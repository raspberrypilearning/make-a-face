## اختر شكلاً

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
هل لديك فكرة عن نوع الوجه أو القناع الذي تريد صنعه؟ استخدم هذه الخطوة لتخطيط فنك وإعداد لوحتك.
</div>
<div>
![منطقة المخرجات مع الهدف وحامل الهدف.] 
(images/vampire.png) {"width="300px:}
</div>
</div>

--- task ---

افتح مشروع البدء [](https://trinket.io/library/trinkets/54d15b9cdf){: target = "_ blank"}. سيتم فتح Trinket في نافذة متصفح أخرى.

--- /task ---

--- task ---

**اختر:** فكر في نوع الوجه الذي تريد صنعه:
+ هل تريد أن تختار شيئًا من تراثك أو ثقافتك الشعبية؟
+ هل سيُظهر فنك إنسانًا أو حيوانًا أو شيئًا أسطوريًا أو ربما آلة؟
+ قد ترغب حتى في إنشاء صورة ذاتية!
+ يمكنك رسم رمز تعبيري لمشاركته مع أصدقائك

--- /task ---

--- task ---

أول شيء يجب فعله عند إنشاء فن باستخدام مكتبة Python `Processing Library` هو إضافة `def setup():` لتعريف دالة `setup` يتم تشغيلها مرة واحدة في بداية البرنامج.

يحتوي مشروع البداية على دالة `setup` تعيّن الحجم `` من لوحتك إلى `400` عرض و `400`طول.

**اختر:** جرب الأرقام وقم بتشغيل التعليمات البرمجية الخاصة بك للعثور على الحجم الذي يناسبك.

--- collapse ---

---
title: ضبط حجم الشاشة عند بدء البرنامج
---

--- code ---
---
language: python filename: main.py - setup() line_numbers: true line_number_start: 6
line_highlights: 7
---
def setup():   
size(400, 400) #400 by 400 works well for a round face

--- /code ---

--- /collapse ---

--- /task ---

--- task ---

**اختر:** فكر في الألوان التي ستستخدمها لوجهك وغيّر </code>خلفية` شاشتك على لون مكمل.</p>

<p spaces-before="0">[[[generic-theory-simple-colours]]]</p>

<p spaces-before="0">--- collapse ---</p>

<hr />

<h2 spaces-before="0">title: ضبط لون الشاشة عند بدء البرنامج</h2>

<p spaces-before="0">--- code ---</p>

<hr />

<p spaces-before="0">language: python
filename: main.py - draw()
line_numbers: true
line_number_start: 9</p>

<h2 spaces-before="0">line_highlights: 9</h2>

<pre><code>background(255, 255, 255) #Try different numbers to change the colour 
`</pre>

--- /code ---

--- /collapse ---

--- /task ---

--- task ---

**نصيحة:** دالة `draw` لها `تعليمة برمجية grid()`. يضيف هذا شبكة إحداثيات على خلفيتك تساعدك على معرفة مكان وضع الميزات على وجهك.

لإيقاف تشغيل الشبكة ، أضف `#` أمام الكود ، ولإعادة تشغيله ، قم بإزالة `#`.

--- code ---
---
language: python
filename: main.py - draw()
---

    grid() #Shows grid

--- /code ---

--- code ---
---
language: python
filename: main.py - draw()
---

    #grid() #Hide grid by turning it into a comment

--- /code ---

--- /task ---

--- task ---

**اختبار:** قم بتشغيل التعليمات البرمجية الخاصة بك لمعرفة لون الخلفية.

--- /task ---


--- task ---

**تصحيح:** قد تجد بعض الأخطاء في مشروعك والتي تحتاج إلى إصلاحها. فيما يلي بعض الأخطاء الشائعة.

--- collapse ---

---
title: لقد قمت بتحديث الحجم واللون ولكن منطقة الإخراج تبقى كما هي
---

بعد تغيير الرمز ، ستحتاج إلى `تشغيل` لمشروعك لمعرفة التغييرات في منطقة الإخراج.

--- /collapse ---

--- collapse ---

---
title: لقد جربت أرقامًا مختلفة ولكن لون الخلفية لا يتغير
---

الحد الأقصى لمقدار اللون الأحمر أو الأخضر أو الأزرق هو</code>255`. تأكد من أن جميع قيم لون الخلفية` الخاصة بك تتراوح بين `0` و</code>255.  </p>

<p spaces-before="0">--- /collapse ---</p>

<p spaces-before="0">--- /task ---</p>

<p spaces-before="0">--- save ---</p>