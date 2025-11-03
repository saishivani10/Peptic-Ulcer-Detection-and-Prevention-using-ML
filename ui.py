import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.scrolledtext import ScrolledText

# Import prediction function from PEP.py
from PEP import predict_symptoms, build_models

# Build models in background to reduce UI lag on first prediction
build_models(verbose=False)

# Simple knowledge base: brief notes and precautions for common diseases
# Keys are normalized disease names (lowercase, alphanumeric only)
DISEASE_INFO = {
    'pepticulcerdiseae': {
        'title': 'Peptic Ulcer Disease',
        'note': 'Peptic ulcers are sores in the stomach or duodenum, often caused by H. pylori infection or long-term NSAID use. They can lead to burning abdominal pain and may worsen on an empty stomach.',
        'precautions': [
            'Avoid NSAIDs unless advised by a clinician',
            'Limit alcohol and stop smoking',
            'Prefer small, frequent meals; avoid very spicy/acidic foods',
            'Take prescribed PPIs/H2 blockers as directed',
            'Seek medical care if you notice black/tarry stools or vomiting blood'
        ]
    },
    'fungalinfection': {
        'title': 'Fungal Infection',
        'note': 'Fungal skin infections commonly cause itchy, red patches. They spread in moist areas and via direct contact.',
        'precautions': [
            'Keep the area clean and dry',
            'Use antifungal creams as recommended',
            'Avoid sharing towels or clothing',
            'Wear breathable fabrics',
            'Consult a clinician if widespread or not improving'
        ]
    },
    'gerd': {
        'title': 'Gastroesophageal Reflux Disease (GERD)',
        'note': 'GERD occurs when stomach acid frequently flows back into the esophagus, causing heartburn and regurgitation.',
        'precautions': [
            'Avoid late-night meals; elevate head of bed',
            'Limit trigger foods: caffeine, mint, chocolate, fatty/spicy meals',
            'Maintain healthy weight and avoid tight clothing',
            'Take PPIs/H2 blockers if prescribed',
            'Seek care if swallowing pain or weight loss occurs'
        ]
    },
    'gastroenteritis': {
        'title': 'Gastroenteritis',
        'note': 'An irritation/infection of the stomach and intestines that causes diarrhea, vomiting, and cramps.',
        'precautions': [
            'Hydrate with oral rehydration solution',
            'Eat bland foods (BRAT: bananas, rice, applesauce, toast)',
            'Avoid dairy, alcohol, and greasy foods temporarily',
            'Practice hand hygiene to prevent spread',
            'Seek care if blood in stool or signs of dehydration'
        ]
    },
    'urinarytractinfection': {
        'title': 'Urinary Tract Infection (UTI)',
        'note': 'UTIs often cause burning urination, frequency, and lower abdominal discomfort. They need appropriate antibiotics.',
        'precautions': [
            'Increase water intake',
            'Do not delay urination; empty bladder fully',
            'Maintain good perineal hygiene',
            'Complete prescribed antibiotics if given',
            'Seek care for fever, flank pain, or recurrent infections'
        ]
    },
    'hypertension': {
        'title': 'Hypertension (High Blood Pressure)',
        'note': 'Chronically elevated blood pressure increases risk of heart, brain, and kidney disease.',
        'precautions': [
            'Reduce salt intake; follow DASH-style diet',
            'Exercise regularly; maintain healthy weight',
            'Limit alcohol; stop smoking',
            'Take medicines as prescribed and check BP regularly',
            'Follow up for kidney/heart risk assessment'
        ]
    },
    'diabetes': {
        'title': 'Diabetes Mellitus',
        'note': 'A metabolic disorder with high blood glucose due to insulin deficiency or resistance.',
        'precautions': [
            'Monitor blood glucose as advised',
            'Adopt balanced diet with portion control',
            'Exercise regularly and maintain healthy weight',
            'Adhere to medications/insulin regimens',
            'Foot care; regular eye and kidney checks'
        ]
    },
    'dengue': {
        'title': 'Dengue Fever',
        'note': 'A mosquito-borne viral illness with high fever, severe aches, and sometimes bleeding risk.',
        'precautions': [
            'Adequate fluids; avoid NSAIDs (use paracetamol unless told otherwise)',
            'Seek care if bleeding, severe abdominal pain, or persistent vomiting',
            'Use mosquito control and nets',
            'Rest until recovery confirmed'
        ]
    },
    'malaria': {
        'title': 'Malaria',
        'note': 'A parasitic infection transmitted by mosquitoes causing fever cycles, chills, and anemia.',
        'precautions': [
            'Seek urgent care for testing and antimalarials',
            'Use bed nets and repellents in endemic areas',
            'Complete full treatment course',
            'Hydrate and rest'
        ]
    },
    'typhoid': {
        'title': 'Typhoid Fever',
        'note': 'A Salmonella Typhi bacterial infection causing high fever, abdominal pain, and diarrhea/constipation.',
        'precautions': [
            'Antibiotics as prescribed; complete the course',
            'Safe water and food hygiene',
            'Hydration and rest',
            'Consider vaccination in risk settings'
        ]
    },
    'commoncold': {
        'title': 'Common Cold',
        'note': 'A self-limited viral infection of the upper respiratory tract with runny nose, cough, and sore throat.',
        'precautions': [
            'Rest and fluids',
            'Saline nasal rinses or steam inhalation',
            'Symptomatic relief as advised; avoid unnecessary antibiotics',
            'Hand hygiene to prevent spread'
        ]
    },
    'pneumonia': {
        'title': 'Pneumonia',
        'note': 'Infection of the lungs that may cause cough, fever, breathlessness, and chest pain.',
        'precautions': [
            'Medical evaluation; antibiotics/antivirals as indicated',
            'Adequate hydration and rest',
            'Monitor warning signs: worsening breathlessness, confusion',
            'Vaccination (flu, pneumococcal) per guidance'
        ]
    }
}

def _norm_key(name: str):
    return ''.join(ch for ch in str(name).lower() if ch.isalnum())

class SymptomSelector(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Peptic Ulcer / Disease Predictor')
        self.geometry('1200x800')
        self.configure(bg='#f7fbff')

        # fetch symptom list from PEP module by calling build_models (cached)
        _, _, _, symptoms, _ = build_models()
        self.symptoms = symptoms

        self.create_widgets()

    def create_widgets(self):
        # colored top banner with a simple drawn emblem
        banner = tk.Canvas(self, height=120, bg='#005f73', highlightthickness=0)
        banner.pack(fill='x')
        # draw a simple stomach-like icon (stylized)
        banner.create_oval(40, 20, 140, 100, fill='#fb8500', outline='')
        banner.create_polygon(80,40, 120,60, 100,90, 60,90, fill='#ffb703', outline='')
        banner.create_text(360, 60, text='Peptic Ulcer / Disease Predictor', font=('Helvetica',20,'bold'), fill='white')

        frm = ttk.Frame(self)
        frm.pack(fill='both', expand=True, padx=12, pady=12)

        # Main container with two sections: symptoms (left, 70%) and controls (right, 30%)
        # Create a framed, colored area with a canvas + scrollbar containing checkbuttons
        left_area = ttk.Frame(frm)
        left_area.pack(side='left', fill='both', expand=True, padx=(0,8))
        
        lbl = ttk.Label(left_area, text='Select the symptoms you are experiencing:')
        lbl.pack(anchor='w', pady=(0,5))
        
        canvas = tk.Canvas(left_area, bg='#e8f6f3')
        canvas.pack(side='left', fill='both', expand=True)

        scrollbar = ttk.Scrollbar(left_area, orient='vertical', command=canvas.yview)
        scrollbar.pack(side='right', fill='y')

        canvas.configure(yscrollcommand=scrollbar.set)

        inner = ttk.Frame(canvas, relief='flat')
        canvas.create_window((0,0), window=inner, anchor='nw')

        self.vars = []
        # use a four-column layout for checkbuttons to show all symptoms
        col = 0
        row = 0
        for idx, s in enumerate(self.symptoms):
            v = tk.IntVar(value=0)
            chk = ttk.Checkbutton(inner, text=s.replace('_',' '), variable=v)
            chk.grid(row=row, column=col, sticky='w', padx=6, pady=2)
            self.vars.append((s, v))
            row += 1
            if row >= 35:  # 35 rows per column to fit all symptoms
                row = 0
                col += 1
        
        # Update scroll region after all widgets are added
        inner.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox('all'))
        
        # Enable mousewheel scrolling
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)

        # Algorithm selection and right pane (fixed width, not expanding)
        right_area = ttk.Frame(frm, width=450)
        right_area.pack(side='right', fill='y', padx=(8,0))
        right_area.pack_propagate(False)  # Prevent shrinking

        alg_frm = ttk.LabelFrame(right_area, text='Options', padding=8)
        alg_frm.pack(fill='x', padx=6, pady=6)
        ttk.Label(alg_frm, text='Algorithm:').pack(side='left')
        self.alg_var = tk.StringVar(value='auto')
        alg_combo = ttk.Combobox(alg_frm, textvariable=self.alg_var, values=['auto (recommended)','tree','random','gnb'], state='readonly')
        alg_combo.pack(side='left', padx=5)

        # Predict button
        btn = ttk.Button(right_area, text='Predict', command=self.on_predict)
        btn.pack(pady=12, fill='x', padx=8)

        # Help text
        help_lbl = ttk.Label(right_area, wraplength=420, text='Tip: Use Auto recommended for best result. Select symptoms and click Predict.')
        help_lbl.pack(padx=8, pady=(6,12))

        # Result area (styled) - text only
        res_frame = ttk.LabelFrame(right_area, text='Result')
        res_frame.pack(fill='both', padx=8, pady=6, expand=True)
        
        # Text result only
        self.result_txt = ScrolledText(res_frame, height=12, width=50, wrap='word')
        self.result_txt.pack(side='top', fill='both', expand=True, padx=6, pady=6)

    def on_predict(self):
        selected = [s for s, v in self.vars if v.get()==1]
        if not selected:
            messagebox.showinfo('No symptoms', 'Please select at least one symptom')
            return
        alg = self.alg_var.get()
        # map friendly 'auto (recommended)' to ensemble voting
        if alg.lower().startswith('auto'):
            # query each algorithm and perform majority vote
            p1 = predict_symptoms(selected, algorithm='tree')
            p2 = predict_symptoms(selected, algorithm='random')
            p3 = predict_symptoms(selected, algorithm='gnb')
            votes = [p for p in (p1,p2,p3) if p]
            if not votes:
                pred = None
            else:
                # majority vote
                from collections import Counter
                cnt = Counter(votes)
                pred, cntv = cnt.most_common(1)[0]
                # If tie (e.g. three different), fall back to tree's prediction
                if cntv == 1 and len(set(votes)) > 1:
                    pred = p1
        else:
            pred = predict_symptoms(selected, algorithm=alg)
        if pred:
            # display text only with brief note and precautions
            ulcer_type = self._detect_ulcer_type(pred)
            nkey = _norm_key(pred)
            info = DISEASE_INFO.get(nkey)

            # Generic fallbacks if not in dictionary
            title = (info.get('title') if info else pred)
            note = (info.get('note') if info else 'This prediction indicates a likely condition based on your selected symptoms. Please consult a licensed clinician for confirmation and treatment advice.')
            precautions = (info.get('precautions') if info else [
                'Monitor symptoms and seek medical advice if they persist or worsen',
                'Avoid self-medication; use over-the-counter drugs only as advised',
                'Stay hydrated and rest adequately'
            ])

            lines = []
            lines.append(f'Predicted disease: {title}')
            if ulcer_type:
                lines.append(f'Ulcer type: {ulcer_type}')
            lines.append('')
            lines.append('About:')
            lines.append(f'  - {note}')
            lines.append('')
            lines.append('Precautions:')
            for p in precautions:
                lines.append(f'  - {p}')

            self.result_txt.delete('1.0', tk.END)
            self.result_txt.insert(tk.END, '\n'.join(lines) + '\n')
        else:
            messagebox.showerror('Prediction failed', 'Could not predict disease for the selected symptoms')

    def _detect_ulcer_type(self, pred_name: str):
        if not pred_name:
            return None
        n = pred_name.lower().replace(' ', '')
        if 'ulcer' in n or 'peptic' in n:
            return 'Peptic ulcer'
        return None

if __name__ == '__main__':
    app = SymptomSelector()
    app.mainloop()
