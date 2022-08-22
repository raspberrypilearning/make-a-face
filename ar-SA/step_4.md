## أضف العيون

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
العيون تجعل الشكل يبدأ ليبدو كوجه.
</div>
<div>
! [منطقة المخرجات تظهر هدفًا بخمس دوائر.](images/five_circles.png){:width="300px"}
</div>
</div>

--- task ---

فكر في نوع العيون التي يحتاجها وجهك. أبسط العيون عبارة عن دائرتين فقط.

يمكنك إضافة قزحية ملونة مختلفة والتلاميذ. يمكنك إضافة الضوء / الأضواء الخاطفة بلون مختلف.

--- /task ---

جرب `اشكال بيضوية` في دالة `draw` لإنشاء العيون التي تريدها.

--- task ---

### ضع العيون

الرقم الأول في `الشكل البيضوي` هو مركز العين. يجب وضع العينين على نفس المسافة من مركز الرسم.

في هذا المثال ، `160` و</code> 240 `يبعدان بمقدار ` 40 ` عن 200، وهو ما يصلح لرسم بعرض 400. </p>

<p spaces-before="0">--- code ---</p>

<hr />

<p spaces-before="0">language: python</p>

<h2 spaces-before="0">filename: main.py - draw()</h2>

<p spaces-before="2">fill(0, 0, 0) #Black — change to red, green, or blue up to 255
  eye_size = 50
  ellipse(160, 180, eye_size, eye_size) #x, y, width, height
  ellipse(240, 180, eye_size, eye_size)</p>

<p spaces-before="0">--- /code --- </p>

<p spaces-before="0"><strong x-id="1">نصيحة:</strong> إذا كنت تريد عيونًا مستديرة ، فإن استخدام متغير <code>eye_size` يجعل من السهل تغيير عرض وارتفاع كلتا العينين في مكان واحد.

[[[processing-python-ellipse]]]

--- collapse ---

---
title: حساب المراكز على أساس العرض
---

يقع مركز الرسم في الموضع `عرض / 2` أو نصف العرض. يمكنك استخدام هذا لوضع العينين عن طريق طرح عرض العين للعين اليسرى وإضافته للعين اليمنى:

--- code ---
---
language: python
filename: main.py - draw()
---

  fill(0, 0, 0) #Black — change to red, green, or blue up to 255 eye_size = 50 ellipse( (width / 2) - 40, 180, eye_size, eye_size) #x, y, width, height ellipse( (width / 2) + 40 , 180, eye_size, eye_size)

--- /code ---

يمكنك أيضًا حساب عرض العيون بناءً على عرض الرسم.

--- code ---
---
language: python
filename: main.py - draw()
---

  fill(0, 0, 0) #Black — change to red, green, or blue up to 255 ellipse( (width / 2) - (width / 10) , 180, eye_size, eye_size) #x, y, width, height ellipse( (width / 2) + (width / 10) , 180, eye_size, eye_size)

--- /code ---

--- /collapse ---

قم بتغيير الرقم الثاني في استدعاء دالة `ellipse` لتحريك موضع `y` (رأسيًا) للعينين.

--- /task ---

--- task ---

**اختبار:** استمر في تغيير شكل وموضع العينين حتى تعجبك الطريقة التي تبدو بها.

**نصيحة:** إذا قمت بتعيين حد لرسم الوجه ولا تريد رسمًا للعين ، فستحتاج إلى استدعاء `no_stroke ()` قبل رسم العيون.

[[[processing-stroke]]]

--- /task ---

--- task ---

### أضف التفاصيل

يمكنك استخدام المزيد من الدوائر لإنشاء:
+ قزحية ملونة
+ بؤبؤ عين اسود
+ الأضواء البيضاء
+ أو أي شيء آخر

تحتوي هذه العين على قزحية ملونة ، وبؤبؤ أسود ، وأضواء بيضاء متغيرة التعتيم: ![تُظهر منطقة الإخراج عينًا بها أضواء خاطفة على التلميذ والقزحية.](images/catchlights.png)

\[[[generic-theory-simple-colours]]\] \[[[processing-opacity\]]]

يمكنك أيضًا تحريك العيون عن طريق تدويرها.

[[[processing-rotation]]]

--- /task ---

--- task ---

**اختبار:** استمر في تغيير شكل وموضع العينين حتى تعجبك الطريقة التي تبدو بها.

هل بدأ رسمك يبدو كوجه؟

--- /task ---

--- task ---

**تصحيح:** قد تجد بعض الأخطاء في مشروعك والتي تحتاج إلى إصلاحها. فيما يلي بعض الأخطاء الشائعة.

--- collapse ---
---
title: العيون ليست في المنتصف
---

يمكنك استخدام ارتفاع</code> `في المركز.</p>

<p spaces-before="0">--- /collapse ---</p>

<p spaces-before="0">--- collapse ---</p>

<hr />

<h2 spaces-before="0">title: العيون غير محاذية لبعضها البعض</h2>

<p spaces-before="0">إذا كنت تريد محاذاة العينين ، فتأكد من استخدام نفس الرقم للإحداثيات لكلتا العينين. حاول استخدام متغير بحيث تكون القيم هي نفسها دائمًا. </p>

<p spaces-before="0">--- /collapse ---</p>

<p spaces-before="0">--- collapse ---</p>

<hr />

<h2 spaces-before="0">title: لا أستطيع رؤية بؤبؤ العين أو قزحية العين</h2>

<p spaces-before="0">يجب رسم العين أولاً ، ثم القزحية ، وأخيراً التلميذ. الترتيب الذي ترسم به الأشياء مهم جدًا.</p>

<p spaces-before="0">تتكون رسومات الكمبيوتر من طبقات. في عينك ، كل قطع ناقص عبارة عن طبقة. تقع الكائنات الموجودة في الطبقات العليا أمام الكائنات الموجودة في الطبقات السفلية. تخيل قص كل الأشكال من الورق. اعتمادًا على كيفية ترتيب وتداخل تلك الورقة، قد تبدو النتيجة النهائية مختلفة تمامًا.</p>

<p spaces-before="0">--- /collapse ---</p>

<p spaces-before="0">--- collapse ---</p>

<hr />

<h2 spaces-before="0">title: عيني ليست مستديرة</h2>

<p spaces-before="0">الرقمان الثالث والرابع في <code>الشكل البيضوي` هما عرض وارتفاع العينين.

**نصيحة:** إذا جعلتها متشابهة ، فستحصل على عيون مستديرة.

--- /collapse ---


--- /task ---

--- save ---