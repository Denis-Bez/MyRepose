# Автоматический рендеринг страниц

# background, title, expertise_name, description
content = {
    'page_not_found': {'title': 'Страница не найдена'},
    'index': {'title': 'ЭНЕРГО group Экспертиза - Энергия в руках профессионалов. Энергогрупп', 'description': 'Судебные и досудебные независимые экспертизы по всей России. Компания ЭнергоГрупп'},
    'services': {'title': 'Энергогрупп. Заказать экспертизу электротехнических работ и оборудования Энерго group', 'description': 'Независимая экспертиза электротехнического силового оборудования. Экспертиза электротехнических и пусконаладочных работ'},
    'experts': {'title': 'Энергогрупп. Эксперты в области электротехнических работ Энерго group', 'description': 'Независимые эксперты в области электротехнического оборудования. Судебная и досудебная экспертиза'},
    'contacts': {'title': 'Энергогрупп. Отправьте заявку и мы с вами свяжемся Энерго group', 'description': 'Независимая электротехническая экспертиза в городе Перми. Компания ЭнергоГрупп'},
    'privacy': {'title': 'Энергогрупп. Политика конфиденциальности eg-expert.ru', 'description': 'Политика обработки личных данных ЭнергоГрупп'},
    'electric_work': {'background': 'background-default', 'title': 'Энерго group Экспертиза электромонтажных работ', 'expertise_name': 'Электромонтажных работ', 'description': 'Судебная и досудебная экспертиза качества выполнения электромонтажных работ на качество, объем, соответствие проекту и нормативно-технической документации'},
    'launch_work': {'background': 'background-default', 'title': 'Энерго group Экспертиза пусконаладочных работ', 'expertise_name': 'Пусконаладочных работ до 500 кВ', 'description': 'Экспертиза пусконаладочных работ до 500 кВ. Выявление причины аварии или выхода из строя, анализ качества выполненных работ'},
    'equip_condit': {'background': 'background-default', 'title': 'Экспертиза текущего состояния электротехнического оборудования Энерго group', 'expertise_name': 'Текущего состояния электротехнического оборудования', 'description': 'Экспертиза текущего состояния электротехнического оборудования до 500 кВ'},
    'review': {'background': 'background-default', 'title': 'Энерго group. Рецензирование электротехнических экспертиз', 'expertise_name': 'Заключения сторонних экспертов', 'description': 'Проведем рецензию экспертного заключения. Проведем все необходимые испытания и измерения'},
    'accidents': {'background': 'background-default', 'title': 'Энерго group. Выявление причин аварий, коротких замыканий, выхода из строя оборудования', 'expertise_name': 'На выявление причин аварий, коротких замыканий, выхода из строя оборудования', 'description': 'Выявление причин аварий, коротких замыканий, поломок, выхода из строя электротехнического оборудования'},
    'purpose': {'background': 'background-default', 'title': 'Энерго group. Подтверждение электротехнического назначения, качества', 'expertise_name': 'На подтверждение электротехнического назначения оборудования', 'description': 'Подтверждение электротехнического назначения, определение качества электротехнического оборудования, состояния'},
    'react_compensation': {'background': 'background-block2', 'title': 'Экспертиза Устройств компенсации реактивной мощности Энерго group', 'expertise_name': 'Устройств компенсации реактивной мощности', 'description': 'Экспертиза поломки, отказа и выхода из строя Устройств компенсации реактивной мощности'},
    'smooth_start': {'background': 'background-block2', 'title': 'Экспертиза Устройств плавного пуска и частотного регулирования Энерго group', 'expertise_name': 'Устройств плавного пуска (УПП) и частотного регулирования электродвигателей', 'description': 'Независимая судебная и досудебная экспертиза Устройств плавного пуска (УПП) и частотного регулирования электродвигателей'},
    'electric_motor': {'background': 'background-block2', 'title': 'Экспертиза Электродвигателей Энерго group', 'expertise_name': 'Электродвигателей', 'description': 'Электротехническая экспертиза Электродвигателей по всей России'},
    'generator': {'background': 'background-block2', 'title': 'Экспертиза Генераторов и Систем возбуждения генераторов Энерго group', 'expertise_name': 'Генераторов и Систем возбуждения генераторов', 'description': 'Электротехническая экспертиза Генераторов. Экспертиза при выходе оборудования из строя, дефектах и повреждениях'},
    'lighting': {'background': 'background-block2', 'title': 'Экспертиза Систем освещения Энерго group', 'expertise_name': 'Систем освещения и светотехнического оборудования', 'description': 'Заказать судебную и досудебную экспертизу Систем освещения, электротехнического оборудования, светильников, опор освещения'},
    'conductor': {'background': 'background-block2', 'title': 'Экспертиза Токопроводов и шинопроводов Энерго group', 'expertise_name': 'Токопроводов и шинопроводов', 'description': 'Проведем независимую экспертизу Токопроводов и шинопроводов. Осуществим необходимые испытания и измерения'},
    'ground_loop': {'background': 'background-block2', 'title': 'Экспертиза Контура заземления', 'expertise_name': 'Контура заземления', 'description': 'Экспертиза Контура заземления'},
    'switchboard': {'background': 'background-block2', 'title': 'Экспертиза Контура заземления', 'expertise_name': 'Электрощитового оборудования', 'description': 'Заказать независимую экспертизу Электрощитового оборудования'},
    'power_trans': {'background': 'background-block3', 'title': 'Экспертиза Силовых трансформаторов любой мощности Энерго group', 'expertise_name': 'Силовых трансформаторов любой мощности, трансформаторов тока, проведенного ремонта. Обследование текущего состояния трансформаторов', 'description': 'Экспертиза Силовых трансформаторов любой мощности, трансформаторов тока, проведенного ремонта. Обследование текущего состояния трансформаторов'},
    'ktp': {'background': 'background-block3', 'title': 'Экспертиза комплектных трансформаторных подстанций Энерго group', 'expertise_name': 'Комплектных трансформаторных подстанций (КТП)', 'description': 'Экспертиза комплектных трансформаторных подстанций (КТП). Проверка на соответствия нормативно-технической документации'},
    'reactor': {'background': 'background-block3', 'title': 'Экспертиза Силовых реакторов Энерго group', 'expertise_name': 'Силовых реакторов', 'description': 'Экспертиза Силовых реакторов. Проверим объем и качество выполненных работ по монтажу, пусконаладки или ремонту оборудования'},
    'disconnector': {'background': 'background-block3', 'title': 'Экспертиза Разъединителей Энерго group', 'expertise_name': 'Разъединителей', 'description': 'Проведем независимую экспертизу Силовых разъединителей. Экспертиза при выходе оборудования из строя, дефектах и повреждениях'},
    'isolator': {'background': 'background-block3', 'title': 'Экспертиза Изоляторов Энерго group', 'expertise_name': 'Изоляторов', 'description': 'Проведем экспертизу силовых изоляторов в случае выхода из строя или поломки. Проведем все необходимые испытания и измерения'},
    'busbar_support': {'background': 'background-block3', 'title': 'Экспертиза Шинных опор Энерго group', 'expertise_name': 'Шинных опор', 'description': 'Судебная и досудебная экспертиза Шинных опор. Наши эксперты работают по всей России'},
    'busbar_flex': {'background': 'background-block3', 'title': 'Экспертиза Гибкой и жесткой ошиновки Энерго group', 'expertise_name': 'Гибкой и жесткой ошиновки', 'description': 'Электротехническая экспертиза Гибкой и жесткой ошиновки. Экспертиза при выходе оборудования из строя, дефектах и повреждениях'},
    'switchgears': {'background': 'background-block3', 'title': 'Экспертиза Распределительных устройств мощностью от 6 кВ до 500 кВ Энерго group', 'expertise_name': 'Распределительных устройств мощностью от 6 кВ до 500 кВ', 'description': 'Экспертиза поломки, отказа и выхода из строя Распределительных устройств мощностью от 6 кВ до 500 кВ'},
    'cable': {'background': 'background-block4', 'title': 'Экспертиза Кабельной продукции Энерго group', 'expertise_name': 'Кабельной продукции', 'description': 'Независимые экспертизы кабельной продукции, электропроводки, аварийных режимов, коротких замыканий. Экспертиза кабеля, проводов на соответствие нормативно технической документации'},
    'cable_coupling': {'background': 'background-block4', 'title': 'Экспертиза Кабельных концевых и соединительных муфт', 'expertise_name': 'Кабельных силовых муфт', 'description': 'Экспертиза Кабельных муфт. Экспертиза кабельных концевых и соединительных силовых муфт'},
    'cable_lines': {'background': 'background-block4', 'title': 'Экспертиза Кабельных линий электропередач', 'expertise_name': 'Кабельных линий электропередач', 'description': 'Заказать независимую экспертизу кабельных линий элекропередач'},
    'cable_airlines': {'background': 'background-block4', 'title': 'Экспертиза Воздушных линий электропередач (ЛЭП)', 'expertise_name': 'Воздушных линий электропередач', 'description': 'Независимая электротехническая экспертиза воздушных линий электропередач (ЛЭП)'},
    'cell_protection': {'background': 'background-block5', 'title': 'Экспертиза Терминалов защит ячеек 6 кВ Энерго group', 'expertise_name': 'Терминалов защиты ячеек 6 кВ', 'description': 'Независимая судебная и досудебная экспертиза Терминалов защиты ячеек 6 кВ'},
    'transfer_devices': {'background': 'background-block5', 'title': 'Экспертиза Устройств автоматического ввода резерва Энерго group', 'expertise_name': 'Устройств автоматического ввода резерва', 'description': 'Проведем экспертизу Устройств автоматического ввода резерва. Экспертиза при выходе оборудования из строя, дефектах и повреждениях'},
    'transfer_panel': {'background': 'background-block5', 'title': 'Экспертиза Панелей защит трансформаторов Энерго group', 'expertise_name': 'Панелей защит трансформаторов', 'description': 'Электротехническая экспертиза Панелей защит трансформаторов. Экспертиза при выходе оборудования из строя, дефектах и повреждениях'},
    'protection_panel': {'background': 'background-block5', 'title': 'Экспертиза Панелей защит оборудования подстанций до 500 кВ Энерго group', 'expertise_name': 'Панелей защит оборудования подстанций до 500 кВ', 'description': 'Экспертиза поломки, отказа и выхода из строя Панелей защит оборудования подстанций до 500 кВ'},
    'emergency_panel': {'background': 'background-block5', 'title': 'Экспертиза Панелей противоаварийной автоматики Энерго group', 'expertise_name': 'Панелей противоаварийной автоматики', 'description': 'Заказать судебную и досудебную экспертизу Панелей противоаварийной автоматики'},
    'automation_panel': {'background': 'background-block5', 'title': 'Экспертиза Панелей управления и автоматизации подстанций Энерго group', 'expertise_name': 'Панелей управления и автоматизации подстанций', 'description': 'Судебная и досудебная экспертиза Панелей управления и автоматизации подстанций. Работаем по всей России'}
}


# Спам фильтр при отправке заявок
# Проверку спам фильтра можно провести с помощью метода пересечения множеств
spam_filter = {
    'name': ['HenryBeide', 'Mike', 'Julius Sello Malema', 'NikkelonMox', 'MariaFuro', 'JorgeOrilk', 'Aaril', 'Yaseen', 'CrytoBeide', 'Eric Jones'],
    'phone': [],
    'email': ['Semya7213@gmail.ru',],
    'text': ['ОЗОН.ру', 'Wildberries.ру', 'nуmрhоmaniа', 'нимфoманией', 'биceкcyальнa', 'любoвью', '<a href=', '</a>']
}