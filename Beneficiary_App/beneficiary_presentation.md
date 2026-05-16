# 📱 بوابة المستفيدين (Beneficiary App) - المراجعة الشاملة

تمت مراجعة الهيكلة البرمجية لتطبيق المستفيدين سطرًا بسطر، وإليك الخريطة التفصيلية لكل شاشة ووظيفة (Feature-by-Feature) تم تصميمها وهندستها في التطبيق:

## 🔐 1. منظومة التوثيق والأمان (Auth & Security)
- **`login_screen.dart`**: شاشة تسجيل دخول تعتمد على رقم الجوال فقط لسهولة الاستخدام، مع التحقق من صحة الرقم (Saudi Format).
- **`otp_screen.dart`**: شاشة التحقق بخطوتين (2FA) لضمان موثوقية المستفيد.
- **`register_screen.dart`**: شاشة تسجيل مستخدم جديد للجمعية.
- **`biometric_lock_screen.dart`**: **ميزة استثنائية** لحماية التطبيق بالبصمة البيومترية (الوجه / الإصبع) عند عودة التطبيق من الخلفية.

## 🚀 2. التهيئة والتسجيل (Onboarding & Registration)
- **`onboarding_screen.dart`**: شاشات تعريفية متحركة (Animations) لشرح مزايا التطبيق للمستخدم الجديد.
- **`registration_wizard_screen.dart`**: معالج تسجيل احترافي مقسم إلى 5 مراحل متتالية لمنع تشتت المستخدم:
  - `step1_father_screen.dart`: بيانات الأب.
  - `step2_mother_screen.dart`: بيانات الأم.
  - `step3_attachments_screen.dart`: رفع المستندات الرسمية بآلية ضغط الصور وتوفير المساحة.
  - `step4_children_screen.dart`: إضافة الأبناء.
  - `step5_address_screen.dart`: تحديد العنوان الوطني والسكن.

## 🏠 3. الشاشة الرئيسية والمالية (Home & Finances)
- **`home_screen.dart`**: لوحة القيادة الخاصة بالأسرة.
- **`financial_summary_card.dart`**: بطاقة بنكية الطابع تعرض إجمالي الدعم المصروف للأسرة (ر.س) بتصميم زجاجي (Glassmorphism).

## 👨‍👩‍👧‍👦 4. ملف الأسرة (Family Profile)
- **`family_profile_screen.dart`**: استعراض شامل لحالة الملف (مقبول، مرفوض، قيد الدراسة).
- **`member_detail_screen.dart`**: تفاصيل كل فرد (التعليم، الصحة، العمر).
- **`digital_card_screen.dart`**: **ميزة استثنائية**، بطاقة رقمية بـ QR Code لتعريف المستفيد في الشراكات أو المستودعات الخيرية.

## 📦 5. منظومة الخدمات (Services)
- **`service_catalog_screen.dart`**: متجر لخدمات الجمعية بتصنيفات واضحة.
- **`services_list_screen.dart`**: متابعة حالات الطلبات السابقة للأسرة (Timeline).
- **`service_detail_screen.dart`**: تفاصيل الطلب مع تتبع الإنجاز.
- **`service_create_sheet.dart`**: نموذج ديناميكي منبثق (BottomSheet) لتقديم طلب جديد بسهولة.

## 📚 6. التدريب والتطوير (Training)
- **`training_list_screen.dart`**: استعراض برامج التأهيل المتاحة لأفراد الأسرة.
- **`training_detail_screen.dart`**: التسجيل المباشر في الدورة التدريبية.

## 💬 7. التواصل المباشر (Communication)
- **`chat_screen.dart`**: محادثة فورية ومباشرة مع باحث الأسرة، تدعم إرسال النصوص والمرفقات.
- **`complaints_list_screen.dart`**: منصة لرفع الشكاوى بسرية تامة ومتابعة الردود من الإدارة.

## 🔔 8. الإشعارات الذكية (Smart Notifications)
- **`notifications_screen.dart`**: مركز الإشعارات الذي يستقبل كافة التنبيهات من Odoo. مزود بـ **Deep Linking** لتوجيه المستخدم فوراً للخدمة أو المحادثة المقصودة بضغطة زر.
