## شكل الوجه

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
ارسم ولون شكلاً لوجهك أو قناعك. لا تقم بإضافة الميزات الأخرى حتى الآن ، فستظهر لاحقًا.
</div>
<div>
! [صورة روبوت ذو وجه مربع.] (images / robot-tooth.png) {: width = "200px"}
</div>
</div>

--- task ---

حدد الشكل الرئيسي للوجه لقناعك. يمكن أن تكون دائرة أو قطع ناقص أو مستطيل أو حتى مثلث.

أضف رمزًا إلى الوظيفة `draw ()` لرسم وجه أو قناع. تأكد أيضًا من إزالة `تمرير` من داخل الوظيفة.

يرسم هذا المثال دائرة في المنتصف ، لكن الأمر متروك لك بشأن الشكل الذي تريد استخدامه.

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 11
line_highlights: 12
---

def draw():   
ellipse(width/2, height/2, 200, 200) #Circle in the middle

--- /code ---

![تظهر منطقة الإخراج دائرة سوداء في منتصف الشبكة.](images/black-circle.png)

[[[processing-python-ellipse]]]


[[[processing-python-rect]]]


[[[processing-python-triangle]]]

--- /task ---

--- task ---

**اختبار:** قم بتشغيل التعليمات البرمجية الخاصة بك وقم بتغييرها للحصول على حجم وشكل الوجه الذي تريده.

--- /task ---

--- task ---

اختر لون حد للمخطط ولون تعبئة للجزء الرئيسي من الشكل.

[[[processing-stroke]]]

إذا كنت لا تريد مخططًا تفصيليًا ، فاستخدم `no_stroke ()`.

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 11
line_highlights: 13
---

def draw(): stroke(0) #You can also use no_stroke() fill(255, 255, 0) #Bright yellow ellipse(width/2, height/2, 200, 200) #Circle in the middle

--- /code ---

[[[generic-theory-simple-colours]]]

--- /task ---

--- task ---

**اختبار:** قم بتشغيل الكود الخاص بك وقم بتغيير اللون حتى تشعر بالرضا عنه.

--- /task ---

--- save ---
