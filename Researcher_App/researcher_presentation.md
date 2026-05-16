# 🔎 تطبيق الباحث الميداني (Researcher App) - المراجعة الشاملة

تم تصميم هذا التطبيق ليكون "مكتباً متنقلاً" للباحث الميداني، مزوداً بأدق أدوات الرقابة والإنتاجية. إليك الخريطة التفصيلية للوظائف والشاشات (Feature-by-Feature):

## 🔐 1. التوثيق المتقدم (Advanced Auth)
- **`login_screen.dart` & `otp_screen.dart`**: تسجيل دخول مشفر عبر OTP لضمان عدم دخول أي أطراف غير مصرح لها.
- **`biometric_lock_screen.dart`**: قفل التطبيق الإلزامي ببصمة الباحث حمايةً لبيانات الأسر الحساسة التي يحملها جهازه.

## 📊 2. لوحة القيادة الذكية (Smart Dashboard)
- **`dashboard_screen.dart`**: شاشة رئيسية تعطيك ملخصاً يومياً للمهام (Daily Brief).
- **`stats_grid.dart`**: شبكة إحصائيات بالأرقام (الزيارات المتبقية، الطلبات العاجلة).
- **`urgent_alerts_carousel.dart`**: شريط متحرك (Carousel) يعرض الملفات ذات الأولوية القصوى التي تحتاج لتدخل سريع.
- **الرسوم البيانية (`distribution_chart.dart` & `performance_chart.dart`)**: مؤشرات أداء الباحث وقياس إنجازه.
- **`families_map_widget.dart`**: خريطة حرارية/جغرافية مصغرة تعرض التوزيع المكاني للأسر في نطاق الباحث.

## 🗺️ 3. منظومة الزيارات الميدانية (Visits Lifecycle & Geo-fencing)
- **`visits_list_screen.dart`**: جدولة الزيارات (اليوم، غداً، متأخرة).
- **`visit_detail_screen.dart`**: شاشة إدارة الزيارة بالكامل، تحتوي على أزرار (بدء، إنهاء، تواصل).
- **`visit_timer_widget.dart`**: مؤقت تفاعلي يحسب مدة بقاء الباحث في الموقع.
- **`visits_map_widget.dart`**: ربط مباشر مع خرائط الجهاز للوصول لمنزل الأسرة.
- **الرقابة المكانية (Geofencing)**: النظام يرفض أداء الزيارة إذا كان الباحث خارج نطاق الـ 1 كيلومتر من سكن الأسرة.

## 📂 4. إدارة سجلات الأسر (Families CRM)
تعتبر صفحة `family_detail_screen.dart` نظام CRM متكامل في الجوال، مقسمة إلى أجزاء (Sections) ذكية:
- **`general_info_section.dart`**: البيانات الأساسية (الاسم، الجوال، الفروع).
- **`housing_info_section.dart`**: بيانات السكن والإيجارات والصور الخاصة بالمنزل.
- **أقسام العائلة**: `father_info_section.dart`، `mother_info_section.dart`، `members_list_section.dart`.
- **`financial_info_section.dart`**: الدخل الشهري، الالتزامات، وحساب الاحتياج آلياً.
- **`family_timeline_section.dart`**: خط زمني (Timeline) يسرد قصة الأسرة وتفاعلاتها التاريخية مع الجمعية.
- **`family_action_sheets.dart`**: أزرار إجراءات سريعة لتغيير حالة الأسرة (اعتماد، إرجاع لاستكمال النواقص).

## 🛒 5. خدمات وتوزيعات (Services & Seasonal)
- **`service_detail_screen.dart`**: مراجعة طلبات الأسر مقسمة لـ 4 تبويبات احترافية: 
  - `service_basic_info_tab.dart` (معلومات الطلب)
  - `service_financial_tab.dart` (تأثير الطلب مالياً)
  - `service_specialized_tab.dart` (التقييم الفني للطلب)
  - `service_opinion_attachments_tab.dart` (قرار الباحث).
- **`seasonal_list_screen.dart` & `delivery_screen.dart`**: نظام خاص لإدارة توزيع حملات (رمضان، الشتاء)، يدعم قراءة QR Code لتسليم المساعدات العينية من المستودع.

## 📬 6. الاتصال والإشعارات (Communication & Notifications)
- **`conversations_list_screen.dart` & `chat_screen.dart`**: صندوق بريد مخصص لتواصل الباحث مع الأسر التي يشرف عليها حصرياً.
- **`notifications_screen.dart`**: إشعارات (Push) ثنائية الاتجاه، تصل للباحث فور تحديث الأسرة لبياناتها أو تقديمها لطلب جديد، مع رابط مباشر للشاشة المطلوبة (Deep Linking).
- **`complaints_list_screen.dart`**: الاطلاع على الشكاوى الخاصة بالباحث للرد عليها وتحسين الجودة.
