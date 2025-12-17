from nicegui import ui

# --- بيانات اختبار MBTI ---
MBTI_QUESTIONS = [
    ["أتحمل الزحام والضوضاء", "أتجنب الضوضاء و أبحث عن الهدوء"],
    ["أتكلم أكثر و أنصت أقل", "أنصت أكثر و أتكلم أقل"],
    ["أحب أن أنقل حماستي للناس", "أحتفظ بحماسي داخل نفسي"],
    ["أفقد تركيزي بسهولة", "أستطيع أن أركز جيدا"],
    ["أتقابل مع الناس بسهولة وأشترك في الكثير من الانشطة", "أتحرك وأقابل الناس بحرص وأركز على بعض الانشطة"],
    ["أتفوه بأشياء ثم أفكر لاحقا", "أفكر جيدا قبل أن أتكلم"],
    ["أكره أن أجلس بلا شئ أفعله", "أحتاج وقت مع نفسي لأعيد شحن نفسي"],
    ["أميل للكلام والعمل وسط جماعة", "أفضل التعامل مع أشخاص قليلين وأن أعمل منفردا"],
    ["أحب أن أكون مركز إهتمام", "أسعد بوجودي خارج دائرة الضوء"],
    ["أتعلم أشياء جديدة من خلال التقليد والملاحظة", "أتعلم أشياء جديدة من خلال المبادئ والنظريات"],
    ["أقدر االطرق المعروفة لعمل الاشياء", "أقدر الطرق الجديدة والمبتكرة لعمل الاشياء"],
    ["أركز أكثر على الخبرات السابقة", "أركز أكثر على الاحتمالات"],
    ["أميل لأن أكون واضحا ومحددا وأعطي مواصفات دقيقة", "أميل لأن أكون خياليا و عاما وأعطي أمثلة ومقارنات"],
    ["أعتمد على خبراتي السابقة", "أعتمد على خيالي"],
    ["أحب العلاقات المتوقعة", "أقدر التغيرات في العلاقات"],
    ["أقدر الطرق التقليدية المضمونة لحل المشاكل", "أستخدم الحلول الجديدة المبتكرة"],
    ["أميل لإستخدام المناهج بدقة", "أميل لإستخدام طرق جديدة"],
    ["أقدر المنطق والحقائق", "أقدر الخيال والابتكار"],
    ["أسعى للحق", "أسعى للتناغم"],
    ["أقدر بعقلي أكثر من قلبي", "أقرر بقلبي أكثر من عقلي"],
    ["أتسائل عن نتائج الاخرين (لانهم قد يكونوا مخطئين)", "أقبل أراء الاخرين لانهم بشر ويجب أن نسمعهم"],
    ["ألاحظ التفكير غير المنطقي", "ألاحظ إحتياجات الاخرين"],
    ["أقدر واختار الصراحة أكثر من اللباقة", "أقدر وأختار اللباقة أكثر من الصراحة"],
    ["أتعامل مع الناس بحزم عندما يحتاجون", "أتعامل مع الناس بحب وحنان"],
    ["ألاحظ إيجابيات وسلبيات أي إختيار", "ألاحظ قيمة أي إختيار وتأثيره على البشر"],
    ["ناقد أرى عيوب الاخرين", "أظهر القبول وأحب أن أرضي الاخرين"],
    ["المشاعر مقبولة فقط إذا كانت منطقية", "أي شعور مقبول"],
    ["أفضل أن أقرر لحياتي و أفرض إرادتي عليها", "أتأقلم مع حياتي أينما تأتي بي الظروف"],
    ["أفضل أن أعرف ما أنا مقبل عليه مسبقا", "أفضل التأقلم مع الظروف الجديدة"],
    ["أشعر اني في حالة أفضل بعد أن أتخذ قرار", "أترك النهايات مفتوحة (لا أكمل الكثير من الاعمال)"],
    ["أسعد بإنجاز المهام والانتهاء منها", "أسعد بأن أبدأ الاشياء"],
    ["أحب أن أخطط وأنظم لحياتي بوضوح وتفاصيل", "أريد أن تكون حياتي مرنة جدا"],
    ["لا أحب المفاجات وأفضل التنبيهات المسبقة والمتوقعة", "أستمتع بالمفاجأت والتغيرات في اللحظة الاخيرة"],
    ["أرى الوقت كمورد محدد وألتزم بمواعيد التسليم", "أرى الوقت كمورد متجدد وأحب مرونة مواعيد التسليم"],
    ["أفضل أن أشطب ما أنجزه من قائمة ما يجب فعله", "أتجاهل قائمة ما يجب فعله اليوم حتى إن كتبتها"],
    ["أفضل أن أخطط لما أعمله أولا بأول", "أحب أن أقوم بالمهام واحدة تلو الاخرى بأي ترتيب تظهر به"]
]

MBTI_CATEGORIES = [["E", "I"]]*9 + [["S", "N"]]*9 + [["T", "F"]]*9 + [["J", "P"]]*9

# --- بيانات اختبار الذكاءات ---
INTEL_QUESTIONS = [
    ("يسهل علي تأليف القصص", "ذكاء لغوي"),
    ("عندما أتحدث إلى أحد أنصت إلى الكلمات التي يستخدمها وليس فقط لما يعنيه", "ذكاء لغوي"),
    ("استمتع بحل الكلمات المتقاطعة", "ذكاء لغوي"),
    ("يسهل علي تذكر أسماء الناس والأماكن والتواريخ", "ذكاء لغوي"),
    ("يمكنني اقناع الآخرين برأيي بسهولة", "ذكاء لغوي"),
    ("أستمتع بالألعاب والتمارين التي تعتمد على المنطق والأرقام", "ذكاء منطقي رياضي"),
    ("أستطيع إجراء العمليات الحسابية في ذهني بسرعة", "ذكاء منطقي رياضي"),
    ("أحب تنظيم الأشياء في فئات أو تصنيفات", "ذكاء منطقي رياضي"),
    ("أهتم بالاكتشافات العلمية الجديدة", "ذكاء منطقي رياضي"),
    ("أستمتع بحل المشكلات المعقدة", "ذكاء منطقي رياضي"),
    ("أحتاج دائماً للنقر بأصابعي أو إصدار إيقاعات أثناء العمل", "ذكاء موسيقي"),
    ("أستطيع تمييز الإيقاعات الموسيقية بسهولة", "ذكاء موسيقي"),
    ("أحب الاستماع للموسيقى أثناء الدراسة أو العمل", "ذكاء موسيقي"),
    ("يمكنني العزف على آلة موسيقية أو الغناء بشكل جيد", "ذكاء موسيقي"),
    ("أتذكر ألحان الأغاني بسهولة", "ذكاء موسيقي"),
    ("أستمتع بالأنشطة البدنية مثل الرياضة أو الرقص", "ذكاء حركي"),
    ("أجد صعوبة في الجلوس لفترات طويلة", "ذكاء حركي"),
    ("أحب العمل بيدي في أشياء مثل النحت أو النجارة", "ذكاء حركي"),
    ("أستخدم لغة جسدي بكثرة للتعبير عن مشاعري", "ذكاء حركي"),
    ("أفضل ممارسة الأشياء بنفسي بدلاً من القراءة عنها", "ذكاء حركي"),
    ("أحب رسم المخطط والصور لتوضيح أفكاري", "ذكاء بصري مكاني"),
    ("أستمتع بالألغاز البصرية والمتاهات", "ذكاء بصري مكاني"),
    ("يمكنني تخيل الأشياء في ذهني بسهولة", "ذكاء بصري مكاني"),
    ("أحب استخدام الألوان في تنظيم ملاحظاتي", "ذكاء بصري مكاني"),
    ("أستطيع قراءة الخرائط والرسوم البيانية بسهولة", "ذكاء بصري مكاني"),
    ("أفضل العمل في مجموعات بدلاً من العمل منفرداً", "ذكاء اجتماعي"),
    ("يلجأ إليّ أصدقائي لطلب النصيحة", "ذكاء اجتماعي"),
    ("أستطيع قراءة مشاعر الآخرين من تعابير وجوههم", "ذكاء اجتماعي"),
    ("أحب تكوين صداقات جديدة باستمرار", "ذكاء اجتماعي"),
    ("أستمتع بتعليم الآخرين أشياء جديدة", "ذكاء اجتماعي"),
    ("أفضل العمل بمفردي في معظم الأوقات", "ذكاء ذاتي"),
    ("أعرف نقاط قوتي وضعفي جيداً", "ذكاء ذاتي"),
    ("أقضي وقتاً في التفكير في مستقبلي وأهدافي", "ذكاء ذاتي"),
    ("أحب تدوين يومياتي ومشاعري الخاصة", "ذكاء ذاتي"),
    ("أعتمد على حدسي ومشاعري الداخلية في اتخاذ القرارات", "ذكاء ذاتي"),
]

class UnifiedTestApp:
    def __init__(self):
        self.mbti_idx = 0
        self.mbti_answers = ""
        self.intel_idx = 0
        self.intel_scores = {k: 0 for k in ["ذكاء لغوي", "ذكاء منطقي رياضي", "ذكاء موسيقي", "ذكاء حركي", "ذكاء بصري مكاني", "ذكاء اجتماعي", "ذكاء ذاتي"]}

        ui.query('body').style('direction: rtl; font-family: sans-serif; background-color: #f0f2f5;')
        
        with ui.header().classes('bg-slate-800 items-center justify-between p-4'):
            ui.label('منصة تحليل الشخصية والذكاء').classes('text-2xl text-white font-bold')
            with ui.tabs() as self.tabs:
                self.tab_mbti = ui.tab('نمط الشخصية MBTI')
                self.tab_intel = ui.tab('الذكاءات المتعددة')

        with ui.tab_panels(self.tabs, value=self.tab_mbti).classes('w-full bg-transparent'):
            with ui.tab_panel(self.tab_mbti):
                self.mbti_container = ui.column().classes('w-full items-center mt-6')
                self.render_mbti()
            
            with ui.tab_panel(self.tab_intel):
                self.intel_container = ui.column().classes('w-full items-center mt-6')
                self.render_intel()

    # --- MBTI Logic ---
    def render_mbti(self):
        self.mbti_container.clear()
        with self.mbti_container:
            with ui.card().classes('w-full max-w-lg p-8 items-center shadow-lg'):
                if self.mbti_idx < len(MBTI_QUESTIONS):
                    ui.label('اختبار نمط MBTI').classes('text-2xl font-bold text-blue-800 mb-2')
                    
                    # حساب النسبة المئوية للتقدم
                    progress = self.mbti_idx / len(MBTI_QUESTIONS)
                    ui.linear_progress(value=progress).classes('w-full mb-2')
                    # إظهار النسبة المئوية كعدد صحيح
                    ui.label(f"التقدم: {int(progress * 100)}% ({self.mbti_idx} من {len(MBTI_QUESTIONS)})").classes('text-gray-500 mb-6')
                    
                    q = MBTI_QUESTIONS[self.mbti_idx]
                    ui.button(q[0], on_click=lambda: self.handle_mbti(0)).props('outline').classes('w-full py-4 mb-3 text-lg')
                    ui.button(q[1], on_click=lambda: self.handle_mbti(1)).props('outline').classes('w-full py-4 text-lg')
                else:
                    self.show_mbti_result()

    def handle_mbti(self, choice):
        self.mbti_answers += MBTI_CATEGORIES[self.mbti_idx][choice]
        self.mbti_idx += 1
        self.render_mbti()

    def show_mbti_result(self):
        counts = {c: self.mbti_answers.count(c) for c in "EISNTFJP"}
        res = ("E" if counts.get("E", 0) >= counts.get("I", 0) else "I") + \
              ("S" if counts.get("S", 0) >= counts.get("N", 0) else "N") + \
              ("T" if counts.get("T", 0) >= counts.get("F", 0) else "F") + \
              ("J" if counts.get("J", 0) >= counts.get("P", 0) else "P")
        ui.label('نمط شخصيتك هو:').classes('text-xl text-gray-600')
        ui.label(res).classes('text-7xl font-black text-blue-600 my-6 bg-blue-50 p-4 rounded')
        ui.button('إعادة الاختبار', on_click=self.reset_mbti).props('flat icon=refresh')

    def reset_mbti(self):
        self.mbti_idx = 0
        self.mbti_answers = ""
        self.render_mbti()

    # --- Intelligence Test Logic ---
    def render_intel(self):
        self.intel_container.clear()
        with self.intel_container:
            with ui.card().classes('w-full max-w-lg p-8 items-center shadow-lg'):
                if self.intel_idx < len(INTEL_QUESTIONS):
                    ui.label('اختبار الذكاءات المتعددة').classes('text-2xl font-bold text-emerald-800 mb-2')
                    
                    # حساب النسبة المئوية للتقدم
                    progress = self.intel_idx / len(INTEL_QUESTIONS)
                    ui.linear_progress(value=progress).classes('w-full mb-2 color-emerald')
                    # إظهار النسبة المئوية كعدد صحيح
                    ui.label(f"التقدم: {int(progress * 100)}% (العبارة {self.intel_idx + 1} من {len(INTEL_QUESTIONS)})").classes('text-gray-500 mb-4')
                    
                    text, _ = INTEL_QUESTIONS[self.intel_idx]
                    ui.label(text).classes('text-2xl text-center font-bold mb-10 min-h-[80px] text-slate-800')
                    
                    with ui.row().classes('w-full justify-between items-center px-4 mb-2'):
                        ui.label('1 (لا ينطبق)').classes('text-sm text-red-500 font-bold')
                        ui.label('5 (ينطبق تماماً)').classes('text-sm text-green-600 font-bold')

                    with ui.row().classes('w-full justify-around mt-4'):
                        for v in range(1, 6):
                            ui.button(on_click=lambda val=v: self.handle_intel(val))\
                                .props(f'fab label="{v}" color="emerald"')\
                                .classes('shadow-md text-white font-bold scale-125')
                else:
                    self.show_intel_result()

    def handle_intel(self, value):
        _, cat = INTEL_QUESTIONS[self.intel_idx]
        self.intel_scores[cat] += value
        self.intel_idx += 1
        self.render_intel()

    def show_intel_result(self):
        ui.label('توزيع نسب الذكاءات:').classes('text-2xl font-bold mb-6 text-emerald-900')
        sorted_scores = sorted(self.intel_scores.items(), key=lambda x: x[1], reverse=True)
        for cat, score in sorted_scores:
            perc = (score / 25) * 100
            with ui.row().classes('w-full items-center mb-3'):
                ui.label(cat).classes('w-32 text-sm font-bold')
                with ui.row().classes('flex-grow bg-gray-200 h-4 rounded-full overflow-hidden'):
                    ui.row().style(f'width: {perc}%;').classes('bg-emerald-500 h-full')
                ui.label(f"{int(perc)}%").classes('ml-2 text-xs')
        ui.button('إعادة الاختبار', on_click=self.reset_intel).props('flat icon=refresh').classes('mt-4')

    def reset_intel(self):
        self.intel_idx = 0
        self.intel_scores = {k: 0 for k in self.intel_scores}
        self.render_intel()

UnifiedTestApp()
ui.run(title="Personality & Intelligence Portal", port=8080)
