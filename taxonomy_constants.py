#!/usr/bin/env python3
"""
Taxonomy Constants - Exam-Specific Taxonomies

Generated on: 2025-11-08 12:04:04
Source: tags/Tags_New.xlsx

Contains exam-specific Subject-Topic-Subtopic taxonomies:
  - TNPSC: 623 unique triplets
  - BANKING: 232 unique triplets
  - SSC_RAILWAYS: 669 unique triplets
"""

from typing import Dict, List


# ===== TNPSC TAXONOMY =====

TNPSC_SUBJECTS: List[str] = [
    "Aptitude",
    "General Science",
    "Geography of India",
    "History, Culture of India and Indian National Movement",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
    "Indian Economy & Development Administration in Tamilnadu",
    "Indian Polity",
    "Reasoning",
]

TNPSC_TRIPLETS: List[str] = [
    "General Science > Physics > Nature of Universe",
    "General Science > Physics > General Scientific laws",
    "General Science > Physics - Mechanics > Force",
    "General Science > Physics - Mechanics > Motion",
    "General Science > Physics - Mechanics > Energy",
    "General Science > Physics - Application > Light",
    "General Science > Physics - Application > Sound",
    "General Science > Physics - Application > Heat",
    "General Science > Physics - Application > Electricity and Magnetism",
    "General Science > Physics - Application > Nuclear Physics",
    "General Science > Physics - Application > Laser",
    "General Science > Physics - Application > Electronics and Communications",
    "General Science > Physics - Application > Properties of matter",
    "General Science > Chemistry > Elements",
    "General Science > Chemistry > Compounds",
    "General Science > Chemistry > Acids, Bases & Salts",
    "General Science > Chemistry > Petroleum Products",
    "General Science > Chemistry > fertilizers, pesticides",
    "General Science > Biology > Main concepts of Life Science",
    "General Science > Biology > Classification of Living Organisms",
    "General Science > Biology > Evolution",
    "General Science > Biology > Genetics",
    "General Science > Biology > Physiology",
    "General Science > Biology > Nutrition",
    "General Science > Biology > Health and Hygiene",
    "General Science > Biology > Human Diseases",
    "General Science > Environment > Environment and ecology",
    "General Science > Latest Inventions in science and technology > Latest inventions in science and technology",
    "General Science > Miscellaneous > Miscellaneous",
    "General Science > Current Affairs > Current Affairs",
    "Geography of India > Location and physiography of India > India: An Introduction",
    "Geography of India > Location and physiography of India > The Himalayas",
    "Geography of India > Location and physiography of India > Indo Gangetic plain",
    "Geography of India > Location and physiography of India > Peninsular plateau",
    "Geography of India > Location and physiography of India > Thar desert",
    "Geography of India > Location and physiography of India > Coastal plains",
    "Geography of India > Location and physiography of India > The islands",
    "Geography of India > Drainage system > Himalayan Rivers",
    "Geography of India > Drainage system > Peninsular Rivers",
    "Geography of India > Drainage system > Lakes- types and lakes in India",
    "Geography of India > Drainage system > Dams and waterfals",
    "Geography of India > Climate of India > Composition of the Atmosphere",
    "Geography of India > Climate of India > Layers of the Atmosphere",
    "Geography of India > Climate of India > Heat Zones of the World",
    "Geography of India > Climate of India > The factors affecting the climate",
    "Geography of India > Climate of India > Indian Monsoon",
    "Geography of India > Natural Vegetation > Classification of forest",
    "Geography of India > Natural Vegetation > Indian State of Forest Report",
    "Geography of India > Natural Vegetation > Biodiversity hotspots in India",
    "Geography of India > Natural Vegetation > Major Threats to Biodiversity",
    "Geography of India > Natural Vegetation > The Protected Areas of India",
    "Geography of India > Natural Vegetation > Specialised projects in India",
    "Geography of India > Agricultural and Soils > Soils of India",
    "Geography of India > Agricultural and Soils > Irrigation",
    "Geography of India > Agricultural and Soils > Agriculture IN INDIA",
    "Geography of India > Agricultural and Soils > Livestock & Fisheries",
    "Geography of India > Minerals and Natural Resources > Classification of Resources",
    "Geography of India > Minerals and Natural Resources > Types of minerals",
    "Geography of India > Minerals and Natural Resources > Industries",
    "Geography of India > Transport - Communication > Road transport",
    "Geography of India > Transport - Communication > Railways",
    "Geography of India > Transport - Communication > Water transport, ports",
    "Geography of India > Transport - Communication > Air transport",
    "Geography of India > Transport - Communication > International trade routes",
    "Geography of India > Transport - Communication > Communication",
    "Geography of India > Social Geography > Population density and distribution",
    "Geography of India > Social Geography > Urbanization",
    "Geography of India > Racial, Linguistic Groups and Major Tribes > Racial Groups",
    "Geography of India > Racial, Linguistic Groups and Major Tribes > Religion",
    "Geography of India > Racial, Linguistic Groups and Major Tribes > Tribal Distribution in world",
    "Geography of India > Racial, Linguistic Groups and Major Tribes > Tribal in India",
    "Geography of India > Racial, Linguistic Groups and Major Tribes > Tribals in Tamilnadu",
    "Geography of India > Racial, Linguistic Groups and Major Tribes > Linguistic Groups",
    "Geography of India > Natural calamity - Disaster Management > Natural disasters",
    "Geography of India > Natural calamity - Disaster Management > Man-made disasters",
    "Geography of India > Natural calamity - Disaster Management > National Disaster Management Authority",
    "Geography of India > Environmental pollution > Pollution",
    "Geography of India > Environmental pollution > Pollutants",
    "Geography of India > Environmental pollution > Classification of Pollutants",
    "Geography of India > Environmental pollution > Types of Pollution",
    "Geography of India > Environmental pollution > Government Initiatives to Combat Pollution",
    "Geography of India > Climate Change > Factors Affecting Climate Change",
    "Geography of India > Climate Change > Evidence for Rapid Climate Change in India",
    "Geography of India > Climate Change > Effects of climate change in India",
    "Geography of India > Climate Change > India’s response to Climate Change",
    "Geography of India > Green energy > Solar Power, Wind Power, Hydropower, Geothermal Energy, Biomass, Biofuels",
    "Geography of India > Green energy > Renewable Energy Potential States in India",
    "Geography of India > Green energy > Achievements of India in the Renewable energy sector",
    "History, Culture of India and Indian National Movement > Indus Valley Civilization > Phases of IVC",
    "History, Culture of India and Indian National Movement > Indus Valley Civilization > Lifestyle of people during IVC",
    "History, Culture of India and Indian National Movement > Indus Valley Civilization > Findings, sites ,  economic activities",
    "History, Culture of India and Indian National Movement > Gupta Period > Sources of Gupta Rule",
    "History, Culture of India and Indian National Movement > Gupta Period > Important rulers and titles adopted by Gupta kings",
    "History, Culture of India and Indian National Movement > Gupta Period > Foreign Travellers Visit - Fahien’s Visit",
    "History, Culture of India and Indian National Movement > Gupta Period > Life under Guptas",
    "History, Culture of India and Indian National Movement > Gupta Period > Post Guptas",
    "History, Culture of India and Indian National Movement > Delhi Sultanate > Early Muslim Invasions",
    "History, Culture of India and Indian National Movement > Delhi Sultanate > Major Dynasties and their rulers",
    "History, Culture of India and Indian National Movement > Delhi Sultanate > Life under Delhi Sultanate",
    "History, Culture of India and Indian National Movement > Mughals > Establishment of Mughal Empire",
    "History, Culture of India and Indian National Movement > Mughals > Akbar",
    "History, Culture of India and Indian National Movement > Mughals > Jahangir and Shah Jahan",
    "History, Culture of India and Indian National Movement > Mughals > Aurangzeb",
    "History, Culture of India and Indian National Movement > Mughals > Life under Mughals",
    "History, Culture of India and Indian National Movement > Mughals > Mughals Contribution",
    "History, Culture of India and Indian National Movement > Marathas > Rise of Marathas under Shivaji",
    "History, Culture of India and Indian National Movement > Marathas > Treaty of Purandar",
    "History, Culture of India and Indian National Movement > Marathas > Sambhaji",
    "History, Culture of India and Indian National Movement > Marathas > Rajaram",
    "History, Culture of India and Indian National Movement > Marathas > Shahu",
    "History, Culture of India and Indian National Movement > Marathas > Peshwas under Maratha empire",
    "History, Culture of India and Indian National Movement > Marathas > Mughals and Marathas conflicts",
    "History, Culture of India and Indian National Movement > Marathas > Anglo-Maratha Wars",
    "History, Culture of India and Indian National Movement > Marathas > Decline of Marathas",
    "History, Culture of India and Indian National Movement > Vijaynagar empire > Dynasties",
    "History, Culture of India and Indian National Movement > Vijaynagar empire > Administration",
    "History, Culture of India and Indian National Movement > Vijaynagar empire > Army and military organisation",
    "History, Culture of India and Indian National Movement > Vijaynagar empire > Social and economic life",
    "History, Culture of India and Indian National Movement > Vijaynagar empire > Social life",
    "History, Culture of India and Indian National Movement > The Bahmani Kingdom > Rulers of the Bahmani Kingdom",
    "History, Culture of India and Indian National Movement > The Bahmani Kingdom > The Five Kingdoms",
    "History, Culture of India and Indian National Movement > The Bahmani Kingdom > Administration",
    "History, Culture of India and Indian National Movement > The Bahmani Kingdom > Contribution to Education",
    "History, Culture of India and Indian National Movement > The Bahmani Kingdom > Art and Architecture",
    "History, Culture of India and Indian National Movement > The Bahmani Kingdom > Decline of Bahmani Kingdom",
    "History, Culture of India and Indian National Movement > South Indian History > Sangam Age",
    "History, Culture of India and Indian National Movement > South Indian History > Life under Sangam Age",
    "History, Culture of India and Indian National Movement > South Indian History > Kalabras",
    "History, Culture of India and Indian National Movement > South Indian History > Pallavas dynasty",
    "History, Culture of India and Indian National Movement > South Indian History > Chalukya Dynasty",
    "History, Culture of India and Indian National Movement > South Indian History > Rashtrakutas Dynasty",
    "History, Culture of India and Indian National Movement > South Indian History > Later Pandyas",
    "History, Culture of India and Indian National Movement > South Indian History > Later Cholas",
    "History, Culture of India and Indian National Movement > Religious development in Medieval India > Sufism",
    "History, Culture of India and Indian National Movement > Religious development in Medieval India > Bhaktism",
    "History, Culture of India and Indian National Movement > Religious development in Medieval India > Sikhism",
    "History, Culture of India and Indian National Movement > Cultural History of India > Art and Culture",
    "History, Culture of India and Indian National Movement > Cultural History of India > Characteristics of Indian Culture",
    "History, Culture of India and Indian National Movement > Cultural History of India > India as a Secular State",
    "History, Culture of India and Indian National Movement > Cultural History of India > Social Harmony",
    "History, Culture of India and Indian National Movement > Ancient India > Vedic Age",
    "History, Culture of India and Indian National Movement > Ancient India > Pre Mauryan Age",
    "History, Culture of India and Indian National Movement > Ancient India > Mauryan Age",
    "History, Culture of India and Indian National Movement > Ancient India > Post Mauryan Age",
    "History, Culture of India and Indian National Movement > Ancient India > Foreign successors of Mauryas",
    "History, Culture of India and Indian National Movement > Advent of Europeans in India > The Portuguese in India",
    "History, Culture of India and Indian National Movement > Advent of Europeans in India > The Dutch in India",
    "History, Culture of India and Indian National Movement > Advent of Europeans in India > The Danes in India",
    "History, Culture of India and Indian National Movement > Advent of Europeans in India > The English",
    "History, Culture of India and Indian National Movement > Advent of Europeans in India > The French",
    "History, Culture of India and Indian National Movement > Advent of Europeans in India > Carnatic Wars",
    "History, Culture of India and Indian National Movement > Advent of Europeans in India > British Expansion In India",
    "History, Culture of India and Indian National Movement > Advent of Europeans in India > Economic Policies of British",
    "History, Culture of India and Indian National Movement > Advent of Europeans in India > Impact of British Administration",
    "History, Culture of India and Indian National Movement > Early uprising against British rule > Tribal Movements",
    "History, Culture of India and Indian National Movement > Early uprising against British rule > Peasant Movements",
    "History, Culture of India and Indian National Movement > Early uprising against British rule > Politico- religious movements",
    "History, Culture of India and Indian National Movement > The Revolt of 1857 > Causes of the Revolt",
    "History, Culture of India and Indian National Movement > The Revolt of 1857 > Centres and Spread of the Revolt",
    "History, Culture of India and Indian National Movement > The Revolt of 1857 > Leaders of the Revolt",
    "History, Culture of India and Indian National Movement > The Revolt of 1857 > Causes of Failure of the Revolt",
    "History, Culture of India and Indian National Movement > The Revolt of 1857 > Nature and Impact of the Revolt",
    "History, Culture of India and Indian National Movement > National Renaissance Social and religious reform movements > Socio-Religious Reforms",
    "History, Culture of India and Indian National Movement > National Renaissance Social and religious reform movements > Muslim reform movements",
    "History, Culture of India and Indian National Movement > National Renaissance Social and religious reform movements > Miscellaneous movements",
    "History, Culture of India and Indian National Movement > National Renaissance Social and religious reform movements > PERSONALITIES",
    "History, Culture of India and Indian National Movement > Indian National Congress (1885 - 1920) > Early Phase Indian National Congress",
    "History, Culture of India and Indian National Movement > Indian National Congress (1885 - 1920) > The Moderate Congress (1885-1905)",
    "History, Culture of India and Indian National Movement > Indian National Congress (1885 - 1920) > Political associations in Bengal, Bombay and Madras GoI Act 1861 and 1892",
    "History, Culture of India and Indian National Movement > Indian National Congress (1885 - 1920) > The Extremist (1905-1920)",
    "History, Culture of India and Indian National Movement > Indian National Congress (1885 - 1920) > Differences between the Moderates and the Extremists",
    "History, Culture of India and Indian National Movement > Indian National Congress (1885 - 1920) > Pre congress campaign",
    "History, Culture of India and Indian National Movement > Indian National Movement - I (1905-1918) > Partition of Bengal (1905)",
    "History, Culture of India and Indian National Movement > Indian National Movement - I (1905-1918) > Swadeshi Movement",
    "History, Culture of India and Indian National Movement > Indian National Movement - I (1905-1918) > Muslim League, 1906",
    "History, Culture of India and Indian National Movement > Indian National Movement - I (1905-1918) > Surat Session of INC, 1907",
    "History, Culture of India and Indian National Movement > Indian National Movement - I (1905-1918) > Indian Council Act (Morley-Minto Act) 1909",
    "History, Culture of India and Indian National Movement > Indian National Movement - I (1905-1918) > Ghadar Party, 1913",
    "History, Culture of India and Indian National Movement > Indian National Movement - I (1905-1918) > Komagata Maru Incident 1914",
    "History, Culture of India and Indian National Movement > Indian National Movement - I (1905-1918) > First world war and its impact",
    "History, Culture of India and Indian National Movement > Indian National Movement - I (1905-1918) > The Lucknow Pact (1916)",
    "History, Culture of India and Indian National Movement > Indian National Movement - II (1918-1929) > Emergence of Gandhi",
    "History, Culture of India and Indian National Movement > Indian National Movement - II (1918-1929) > The Government of India Act, 1919",
    "History, Culture of India and Indian National Movement > Indian National Movement - II (1918-1929) > Rowlatt Act and Jallianwala Bagh Massacre (1919)",
    "History, Culture of India and Indian National Movement > Indian National Movement - II (1918-1929) > Khilafat Movement",
    "History, Culture of India and Indian National Movement > Indian National Movement - II (1918-1929) > The Non-Cooperation Movement (1920-22)",
    "History, Culture of India and Indian National Movement > Indian National Movement - II (1918-1929) > Swarajists and no changers",
    "History, Culture of India and Indian National Movement > Indian National Movement - II (1918-1929) > Nagpur Session of Congress",
    "History, Culture of India and Indian National Movement > Indian National Movement - II (1918-1929) > Swaraj Party and its Evaluation",
    "History, Culture of India and Indian National Movement > Indian National Movement - II (1918-1929) > Muddiman Committee (1924)",
    "History, Culture of India and Indian National Movement > Indian National Movement - II (1918-1929) > Simon Commission (1927)",
    "History, Culture of India and Indian National Movement > Indian National Movement - II (1918-1929) > Bardoli Satyagraha (1928)",
    "History, Culture of India and Indian National Movement > Indian National Movement - II (1918-1929) > Nehru Report (1928)",
    "History, Culture of India and Indian National Movement > Indian National Movement - II (1918-1929) > Jinnah’s Fourteen Points",
    "History, Culture of India and Indian National Movement > Indian National Movement - II (1918-1929) > Calcutta session of INC 1928",
    "History, Culture of India and Indian National Movement > Indian National Movement - II (1918-1929) > Delhi Manifesto",
    "History, Culture of India and Indian National Movement > Indian National Movement - II (1918-1929) > Lahore Session, 1929",
    "History, Culture of India and Indian National Movement > Indian National Movement - II (1918-1929) > Allahabad Address (1930)",
    "History, Culture of India and Indian National Movement > Indian National Movement - II (1918-1929) > Emergence of New Forces during 1920s",
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > Civil Disobedience Movement (1930-1931)",
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > Round Table ConferencE",
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > Gandhi-Irwin Pact, 1931",
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > Karachi session of 1931",
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > Communal Award",
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > Poona Pact, 1932",
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > Government of India Act, 1935",
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > World War II and Indian Nationalism",
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > Resignation of Congress Ministers (1939)",
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > Poona Resolution and Conditional Support to Britain (1941)",
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > August Offer of 1940",
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > The Individual Civil Disobedience",
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > Two-Nation Theory",
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > Demand for Pakistan (1942)",
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > Cripps Mission (1942)",
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > Quit India Movement",
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > Azad Hind Fauj",
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > Indian National Army",
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > I.N.A Trials",
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > Indian Navy Rebellion",
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > Rajagopalachari Formula, 1945",
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > Desai - Liaqat Pact",
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > Cabinet Mission (1946)",
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > Wavell Plan",
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > Jinnah’s Direct Action Resolution",
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > Mountbatten Plan of June 1947",
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > Indian Independence Act 1947",
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > Communalism and Partition",
    "History, Culture of India and Indian National Movement > Emergence of Leaders > B.R. Ambedkar",
    "History, Culture of India and Indian National Movement > Emergence of Leaders > Bhagat Singh",
    "History, Culture of India and Indian National Movement > Emergence of Leaders > Bharathiar",
    "History, Culture of India and Indian National Movement > Emergence of Leaders > V.O. Chidambaranar",
    "History, Culture of India and Indian National Movement > Emergence of Leaders > Jawaharlal Nehru",
    "History, Culture of India and Indian National Movement > Emergence of Leaders > Kamarajar",
    "History, Culture of India and Indian National Movement > Emergence of Leaders > Mahatma Gandhi",
    "History, Culture of India and Indian National Movement > Emergence of Leaders > Maulana Abul Kalam Azad",
    "History, Culture of India and Indian National Movement > Emergence of Leaders > Thanthai Periyar",
    "History, Culture of India and Indian National Movement > Emergence of Leaders > Rajaji",
    "History, Culture of India and Indian National Movement > Emergence of Leaders > Subash Chandra Bose",
    "History, Culture of India and Indian National Movement > Emergence of Leaders > Rabindranath Tagore",
    "History, Culture of India and Indian National Movement > Emergence of Leaders > Others",
    "History, Culture of India and Indian National Movement > Governor Generals During British India > Governor of Bengal (Before 1773)",
    "History, Culture of India and Indian National Movement > Governor Generals During British India > Governor Generals of Bengal (1773-1833)",
    "History, Culture of India and Indian National Movement > Governor Generals During British India > Governor Generals of India (1832-1858)",
    "History, Culture of India and Indian National Movement > Governor Generals During British India > Viceroy of India (1858-1947)",
    "History, Culture of India and Indian National Movement > Constitutional Development > Constitutional Development in India",
    "History, Culture of India and Indian National Movement > Civil Services > Development of Civil Services",
    "History, Culture of India and Indian National Movement > Education > Development of Education",
    "History, Culture of India and Indian National Movement > Press > Development of Press",
    "History, Culture of India and Indian National Movement > Prominent personalities in various spheres > Arts, Science, Literature and Philosophy",
    "Indian Polity > Evolution of Indian Constitution > Regulating act of 1773",
    "Indian Polity > Evolution of Indian Constitution > Charter Act of 1833",
    "Indian Polity > Evolution of Indian Constitution > Charter Act of 1853",
    "Indian Polity > Evolution of Indian Constitution > Government of India Act of 1858",
    "Indian Polity > Evolution of Indian Constitution > Indian Councils Act of 1909",
    "Indian Polity > Evolution of Indian Constitution > Government of India Act 1919",
    "Indian Polity > Evolution of Indian Constitution > Government of India Act 1935",
    "Indian Polity > Evolution of Indian Constitution > India Independence Act 1947",
    "Indian Polity > Making of Indian Constiution > Background-Constituent Assembly",
    "Indian Polity > Making of Indian Constiution > Constituent Assembly",
    "Indian Polity > Making of Indian Constiution > Committees (Major & Minor)",
    "Indian Polity > Making of Indian Constiution > Sources of the constitution",
    "Indian Polity > Making of Indian Constiution > Salient features in Indian Constitution",
    "Indian Polity > Preamble > Nature of Indian State",
    "Indian Polity > Preamble > Objectives of the constitution",
    "Indian Polity > Preamble > Significance of the Preamble",
    "Indian Polity > Preamble > Amenability of the Preamble (cases)",
    "Indian Polity > Union, State and Union Territory > Evolution of states and Union territories",
    "Indian Polity > Union, State and Union Territory > Article 1",
    "Indian Polity > Union, State and Union Territory > Article 2",
    "Indian Polity > Union, State and Union Territory > Article 3",
    "Indian Polity > Union, State and Union Territory > Article 4",
    "Indian Polity > Union, State and Union Territory > State reorganization commissions",
    "Indian Polity > Citizenship > Article 5 - 11",
    "Indian Polity > Citizenship > Acquisition of Citizenship",
    "Indian Polity > Citizenship > Loss of Citizenship",
    "Indian Polity > Citizenship > Citizenship Act 1955 and amendments",
    "Indian Polity > Fundamental Rights > Right to equality",
    "Indian Polity > Fundamental Rights > Right to freedom",
    "Indian Polity > Fundamental Rights > Right against exploitation",
    "Indian Polity > Fundamental Rights > Right to freedom of Religion",
    "Indian Polity > Fundamental Rights > Cultural and educational rights",
    "Indian Polity > Fundamental Rights > Rights to constitutional remedies",
    "Indian Polity > Fundamental Rights > Impact on fundamental rights",
    "Indian Polity > Directive Principles of State Policy > Socialistic principles",
    "Indian Polity > Directive Principles of State Policy > Gandhian principles",
    "Indian Polity > Directive Principles of State Policy > Liberal - intellectual principles",
    "Indian Polity > Directive Principles of State Policy > Comparison between DPSP and FRs",
    "Indian Polity > Directive Principles of State Policy > Important Cases related to FR and DPSP",
    "Indian Polity > Directive Principles of State Policy > Important amendments",
    "Indian Polity > Fundamental Duties > Committees",
    "Indian Polity > Fundamental Duties > Article 51A (List of FDs)",
    "Indian Polity > Amendments > Types of amendments",
    "Indian Polity > Amendments > Emergence of the concept of basic structure",
    "Indian Polity > Amendments > Role of judiciary",
    "Indian Polity > Union Executive > President",
    "Indian Polity > Union Executive > Vice President",
    "Indian Polity > Union Executive > Prime Minister",
    "Indian Polity > Union Executive > Central Council of Ministers",
    "Indian Polity > Union Legislature > Rajya Sabha",
    "Indian Polity > Union Legislature > Lok Sabha",
    "Indian Polity > Union Legislature > Members of Parliament",
    "Indian Polity > Union Legislature > Speaker of the Lok Sabha",
    "Indian Polity > Union Legislature > Chairman of Rajya Sabha",
    "Indian Polity > Union Legislature > Parliament - Functioning",
    "Indian Polity > Union Legislature > Bills- enactment/procedure, stages in passing bills etc",
    "Indian Polity > Union Legislature > Budget",
    "Indian Polity > Union Legislature > Powers and functions of parliament Legislative",
    "Indian Polity > Union Legislature > Position of Rajya Sabha",
    "Indian Polity > Union Legislature > Cabinet committees",
    "Indian Polity > Union Legislature > Parliamentary committees",
    "Indian Polity > Union Legislature > Parliamentary forums",
    "Indian Polity > Union Legislature > Parliament privileges",
    "Indian Polity > State Executive > Governor",
    "Indian Polity > State Executive > Comparison between Governor and President",
    "Indian Polity > State Executive > Chief Minister",
    "Indian Polity > State Executive > State council of ministers",
    "Indian Polity > State Legislature > Composition of Two Houses",
    "Indian Polity > State Legislature > Duration of Two Houses",
    "Indian Polity > State Legislature > Powers and functions",
    "Indian Polity > State Legislature > Membership of State Legislature",
    "Indian Polity > State Legislature > Presiding Officers of State Legislature",
    "Indian Polity > State Legislature > Governor assent to bill",
    "Indian Polity > State Legislature > Legislative Procedure in State Legislature",
    "Indian Polity > State Legislature > Position of Legislative Counci",
    "Indian Polity > State Legislature > State legislature comparison with parliament",
    "Indian Polity > State Legislature > Position of state legislative council w.r.t legislative assembly and Rajya Sabha",
    "Indian Polity > State Legislature > Sessions of State Legislature",
    "Indian Polity > Judiciary > Supreme Court",
    "Indian Polity > Judiciary > High court",
    "Indian Polity > Judiciary > Jurisdiction and Power",
    "Indian Polity > Judiciary > Judicial review &  judicial activism",
    "Indian Polity > Judiciary > Subordinate courts",
    "Indian Polity > Local Self Government > Panchayati Raj",
    "Indian Polity > Local Self Government > Municipalities",
    "Indian Polity > Local Self Government > committees",
    "Indian Polity > Centre - State Relationships > Inter-state relation",
    "Indian Polity > Centre - State Relationships > Legislative relations",
    "Indian Polity > Centre - State Relationships > Administrative relations",
    "Indian Polity > Centre - State Relationships > Financial relation",
    "Indian Polity > Centre - State Relationships > Effects of emergencies",
    "Indian Polity > Centre - State Relationships > Committees/Commission related to Centre state relations",
    "Indian Polity > Emergency Provisions > National Emergency",
    "Indian Polity > Emergency Provisions > President’s Rule",
    "Indian Polity > Emergency Provisions > Financial Emergency",
    "Indian Polity > Emergency Provisions > Impact of emergency",
    "Indian Polity > Constitutional Bodies > Election Commission",
    "Indian Polity > Constitutional Bodies > UPSC, SPSC and JPSC",
    "Indian Polity > Constitutional Bodies > National Commissions  SC/ ST/ Backward classes",
    "Indian Polity > Constitutional Bodies > Comptroller and Auditor General of India",
    "Indian Polity > Constitutional Bodies > Attorney General",
    "Indian Polity > Constitutional Bodies > Advocate general",
    "Indian Polity > Constitutional Bodies > Solicitor general",
    "Indian Polity > Non-Constitutional Bodies > National human rights commission & State human rights commission",
    "Indian Polity > Non-Constitutional Bodies > Central information commission & State information commission",
    "Indian Polity > Non-Constitutional Bodies > Central vigilance commission",
    "Indian Polity > Non-Constitutional Bodies > Lokpal and Lokayukta",
    "Indian Polity > Non-Constitutional Bodies > National law commission",
    "Indian Polity > Non-Constitutional Bodies > National green tribunal",
    "Indian Polity > Non-Constitutional Bodies > Food safety and standard authority of India",
    "Indian Polity > Non-Constitutional Bodies > Bureau of Indian standards",
    "Indian Polity > Non-Constitutional Bodies > Competition commission of India",
    "Indian Polity > Non-Constitutional Bodies > Non - Statutory Bodies",
    "Indian Polity > Empowerment of Women > Women Empowerment Schemes in India",
    "Indian Polity > Empowerment of Women > Constitutional Provisions",
    "Indian Polity > Empowerment of Women > Important Acts",
    "Indian Polity > Consumer Protection Forums > Consumer Protection Act 2019",
    "Indian Polity > Political parties and political system in India > Recognised parties",
    "Indian Polity > Political parties and political system in India > non - recognised parties",
    "Indian Polity > Election > Representation of people act 1950 & 1951",
    "Indian Economy & Development Administration in Tamilnadu > Basics of Economy > Microeconomics vs Macroeconomics",
    "Indian Economy & Development Administration in Tamilnadu > Basics of Economy > Sectors of Economy-Primary, Secondary and Tertiary Sector",
    "Indian Economy & Development Administration in Tamilnadu > Basics of Economy > Factors of Production",
    "Indian Economy & Development Administration in Tamilnadu > Basics of Economy > Type of Economic System",
    "Indian Economy & Development Administration in Tamilnadu > Basics of Economy > Growth and Development",
    "Indian Economy & Development Administration in Tamilnadu > Nature of Indian Economy > Strengths of Indian Economy",
    "Indian Economy & Development Administration in Tamilnadu > Nature of Indian Economy > Weakness of Indian Economy",
    "Indian Economy & Development Administration in Tamilnadu > Nature of Indian Economy > Natural Resources",
    "Indian Economy & Development Administration in Tamilnadu > Five-year plan > Economic Planning in India",
    "Indian Economy & Development Administration in Tamilnadu > Five-year plan > Planning Commission of India",
    "Indian Economy & Development Administration in Tamilnadu > Five-year plan > National Development Council (NDC)s",
    "Indian Economy & Development Administration in Tamilnadu > Five-year plan > Five Year Plan",
    "Indian Economy & Development Administration in Tamilnadu > Five-year plan > Niti Aayog",
    "Indian Economy & Development Administration in Tamilnadu > National Income > Basic concepts of national income",
    "Indian Economy & Development Administration in Tamilnadu > National Income > Money",
    "Indian Economy & Development Administration in Tamilnadu > National Income > Money, Demand and Supply",
    "Indian Economy & Development Administration in Tamilnadu > Monetary Policy > Expansionary Vs. Contractionary",
    "Indian Economy & Development Administration in Tamilnadu > Monetary Policy > Objectives of Monetary Policy",
    "Indian Economy & Development Administration in Tamilnadu > Monetary Policy > Composition of the MPC",
    "Indian Economy & Development Administration in Tamilnadu > Monetary Policy > Methods of Credit Control",
    "Indian Economy & Development Administration in Tamilnadu > Monetary Policy > Inflation",
    "Indian Economy & Development Administration in Tamilnadu > Monetary Policy > Meaning of Deflation, Disinflation and Stagflation",
    "Indian Economy & Development Administration in Tamilnadu > Monetary Policy > Measurement of Inflation",
    "Indian Economy & Development Administration in Tamilnadu > Banking > Reserve Bank of India",
    "Indian Economy & Development Administration in Tamilnadu > Banking > Scheduled and Non Scheduled Banks",
    "Indian Economy & Development Administration in Tamilnadu > Banking > Non-Banking Financial Companies(NBFC)",
    "Indian Economy & Development Administration in Tamilnadu > Banking > All India Financial Institutions (AIFI)- Non Banks",
    "Indian Economy & Development Administration in Tamilnadu > Banking > Issue of Banking Sector",
    "Indian Economy & Development Administration in Tamilnadu > Fiscal Policy > Meaning of Public Finance",
    "Indian Economy & Development Administration in Tamilnadu > Fiscal Policy > Budgetary Deficits",
    "Indian Economy & Development Administration in Tamilnadu > Fiscal Policy > Bodies related to Budgeting",
    "Indian Economy & Development Administration in Tamilnadu > Fiscal Policy > Basics of Budget",
    "Indian Economy & Development Administration in Tamilnadu > Fiscal Policy > Components of Budget",
    "Indian Economy & Development Administration in Tamilnadu > Fiscal Policy > Types of Budget",
    "Indian Economy & Development Administration in Tamilnadu > Taxation > Direct Taxes",
    "Indian Economy & Development Administration in Tamilnadu > Taxation > Indirect Taxes",
    "Indian Economy & Development Administration in Tamilnadu > Taxation > GST",
    "Indian Economy & Development Administration in Tamilnadu > Taxation > Miscellaneous",
    "Indian Economy & Development Administration in Tamilnadu > Resource sharing between Union & State Governments > The sources of income as prescribed by the Constitution of India for the Central Government",
    "Indian Economy & Development Administration in Tamilnadu > Resource sharing between Union & State Governments > Earnings of state government",
    "Indian Economy & Development Administration in Tamilnadu > Resource sharing between Union & State Governments > Taxes Levied & Collected by The Union but Assigned to The States",
    "Indian Economy & Development Administration in Tamilnadu > Resource sharing between Union & State Governments > Duties Levied By The Union but Collected & Appropriated by The States",
    "Indian Economy & Development Administration in Tamilnadu > Resource sharing between Union & State Governments > Taxes which are Levied and Collected by the Union but which may be Distributed between the Union and the States",
    "Indian Economy & Development Administration in Tamilnadu > Resource sharing between Union & State Governments > Finance Commission",
    "Indian Economy & Development Administration in Tamilnadu > Structure of Indian Economy & Employment Generation > Main Sectors in India’s Economy",
    "Indian Economy & Development Administration in Tamilnadu > Structure of Indian Economy & Employment Generation > Other Sectors in India’s Economy",
    "Indian Economy & Development Administration in Tamilnadu > Structure of Indian Economy & Employment Generation > Initiatives for Employment Generation",
    "Indian Economy & Development Administration in Tamilnadu > Land Reforms & Agriculture > Role of Agriculture in Indian Economy",
    "Indian Economy & Development Administration in Tamilnadu > Land Reforms & Agriculture > Application of Science and Technology in Agriculture",
    "Indian Economy & Development Administration in Tamilnadu > Land Reforms & Agriculture > Land Reforms",
    "Indian Economy & Development Administration in Tamilnadu > Land Reforms & Agriculture > Cropping Pattern in India",
    "Indian Economy & Development Administration in Tamilnadu > Land Reforms & Agriculture > Types of crops in India",
    "Indian Economy & Development Administration in Tamilnadu > Land Reforms & Agriculture > Major Producer of the Crops in India",
    "Indian Economy & Development Administration in Tamilnadu > Land Reforms & Agriculture > Cropping Seasons in India",
    "Indian Economy & Development Administration in Tamilnadu > Land Reforms & Agriculture > Green Revolution",
    "Indian Economy & Development Administration in Tamilnadu > Land Reforms & Agriculture > Agriculture Related Schemes",
    "Indian Economy & Development Administration in Tamilnadu > Land Reforms & Agriculture > Irrigation",
    "Indian Economy & Development Administration in Tamilnadu > Land Reforms & Agriculture > PDS",
    "Indian Economy & Development Administration in Tamilnadu > Land Reforms & Agriculture > Minimum support prices (MSP), Procurement prices, Issue Price, Retail prices",
    "Indian Economy & Development Administration in Tamilnadu > Land Reforms & Agriculture > Rural Welfare Oriented Programmes",
    "Indian Economy & Development Administration in Tamilnadu > Industrial growth > Types of Industries",
    "Indian Economy & Development Administration in Tamilnadu > Industrial growth > Core Industries in India",
    "Indian Economy & Development Administration in Tamilnadu > Industrial growth > State-wise Distribution of Industries",
    "Indian Economy & Development Administration in Tamilnadu > Industrial growth > Industrial Policies",
    "Indian Economy & Development Administration in Tamilnadu > Industrial growth > Public Sector Enterprises",
    "Indian Economy & Development Administration in Tamilnadu > Rural Welfare Oriented Programmes > Rural Welfare Oriented Programmes",
    "Indian Economy & Development Administration in Tamilnadu > Social Problems > Population",
    "Indian Economy & Development Administration in Tamilnadu > Social Problems > Education",
    "Indian Economy & Development Administration in Tamilnadu > Social Problems > Health",
    "Indian Economy & Development Administration in Tamilnadu > Social Problems > Employment",
    "Indian Economy & Development Administration in Tamilnadu > Social Problems > Poverty",
    "Indian Economy & Development Administration in Tamilnadu > Human Development Index > Three indicators",
    "Indian Economy & Development Administration in Tamilnadu > Human Development Index > Human Development Report",
    "Indian Economy & Development Administration in Tamilnadu > Human Development Index > 5 Indices of Human Development Report",
    "Indian Economy & Development Administration in Tamilnadu > Human Development Index > Important Human Development Indicators of Tamil Nadu",
    "Indian Economy & Development Administration in Tamilnadu > Social Reform Movements in Tamil Nadu > Social Reformers of Tamilnadu",
    "Indian Economy & Development Administration in Tamilnadu > Political parties & Welfare schemes > Political Parties",
    "Indian Economy & Development Administration in Tamilnadu > Political parties & Welfare schemes > Recognized Tamil Nadu State Parties",
    "Indian Economy & Development Administration in Tamilnadu > Political parties & Welfare schemes > Achievements of the Parties",
    "Indian Economy & Development Administration in Tamilnadu > Political parties & Welfare schemes > Social Welfare Schemes by Tamil Nadu",
    "Indian Economy & Development Administration in Tamilnadu > Reservation Policy > Reservation Policy in Tamilnadu",
    "Indian Economy & Development Administration in Tamilnadu > Reservation Policy > Reservation Policy in India",
    "Indian Economy & Development Administration in Tamilnadu > Social Justice & Social Harmony > Social Justice Theories",
    "Indian Economy & Development Administration in Tamilnadu > Social Justice & Social Harmony > Constitutional Provisions of social Justice",
    "Indian Economy & Development Administration in Tamilnadu > Social Justice & Social Harmony > Justice Party Contribution",
    "Indian Economy & Development Administration in Tamilnadu > Social Justice & Social Harmony > Welfare and empowerment of SCs, STs, differently abled, women, transgender, aged and senior citizens, child rights",
    "Indian Economy & Development Administration in Tamilnadu > Social Justice & Social Harmony > Various Commissions",
    "Indian Economy & Development Administration in Tamilnadu > Economic Trends in Tamil Nadu > Highlights of Tamil Nadu Economy",
    "Indian Economy & Development Administration in Tamilnadu > Economic Trends in Tamil Nadu > GI Tags",
    "Indian Economy & Development Administration in Tamilnadu > Economic Trends in Tamil Nadu > Economic Policies",
    "Indian Economy & Development Administration in Tamilnadu > Economic Trends in Tamil Nadu > Budget Highlights",
    "Indian Economy & Development Administration in Tamilnadu > Education and Health Systems in Tamil Nadu > Tamil Nadu Educational System",
    "Indian Economy & Development Administration in Tamilnadu > Education and Health Systems in Tamil Nadu > Literacy in Tamil Nadu",
    "Indian Economy & Development Administration in Tamilnadu > Education and Health Systems in Tamil Nadu > Education & Health Related Constitutional Provisions, Acts, Government Schemes",
    "Indian Economy & Development Administration in Tamilnadu > Education and Health Systems in Tamil Nadu > Education Policy - Tamil Nadu and India",
    "Indian Economy & Development Administration in Tamilnadu > Education and Health Systems in Tamil Nadu > Health Policy - Tamil Nadu and India",
    "Indian Economy & Development Administration in Tamilnadu > Education and Health Systems in Tamil Nadu > Health Systems in Tamil Nadu",
    "Indian Economy & Development Administration in Tamilnadu > Education and Health Systems in Tamil Nadu > Health Indicators",
    "Indian Economy & Development Administration in Tamilnadu > Education and Health Systems in Tamil Nadu > Health Care Institutions in TN - Primary, Secondary and Tertiary",
    "Indian Economy & Development Administration in Tamilnadu > Geography of Tamil Nadu > Physiographic Divisions",
    "Indian Economy & Development Administration in Tamilnadu > Geography of Tamil Nadu > Land Area Extent",
    "Indian Economy & Development Administration in Tamilnadu > Geography of Tamil Nadu > Climate",
    "Indian Economy & Development Administration in Tamilnadu > Geography of Tamil Nadu > Soils",
    "Indian Economy & Development Administration in Tamilnadu > Geography of Tamil Nadu > Natural Vegetation",
    "Indian Economy & Development Administration in Tamilnadu > Geography of Tamil Nadu > Agriculture",
    "Indian Economy & Development Administration in Tamilnadu > Geography of Tamil Nadu > Livestock",
    "Indian Economy & Development Administration in Tamilnadu > Geography of Tamil Nadu > water sources",
    "Indian Economy & Development Administration in Tamilnadu > Geography of Tamil Nadu > Mineral resources",
    "Indian Economy & Development Administration in Tamilnadu > Geography of Tamil Nadu > Industries",
    "Indian Economy & Development Administration in Tamilnadu > Geography of Tamil Nadu > Transport and communication",
    "Indian Economy & Development Administration in Tamilnadu > Geography of Tamil Nadu > Demography",
    "Indian Economy & Development Administration in Tamilnadu > Tamil Nadu e-Governance > Institutional frameworks for e-governance",
    "Indian Economy & Development Administration in Tamilnadu > Tamil Nadu e-Governance > Core Infrastructure of Information Technology",
    "Indian Economy & Development Administration in Tamilnadu > Tamil Nadu e-Governance > e-Governance programs",
    "Indian Economy & Development Administration in Tamilnadu > Tamil Nadu e-Governance > e-governance policy",
    "Indian Economy & Development Administration in Tamilnadu > Achievements of Tamil Nadu in Various Fields > Achievements and Awards",
    "Indian Economy & Development Administration in Tamilnadu > Achievements of Tamil Nadu in Various Fields > E-Governance Initiatives in Tamilnadu",
    "Indian Economy & Development Administration in Tamilnadu > Achievements of Tamil Nadu in Various Fields > Performance of Tamil Nadu Economy",
    "Indian Economy & Development Administration in Tamilnadu > Achievements of Tamil Nadu in Various Fields > Tamil Nadu related recent Survey, data, Indices, Ranking, Reports, etc",
    "Indian Economy & Development Administration in Tamilnadu > Public awareness and General administration > Public awareness and General administration",
    "Indian Economy & Development Administration in Tamilnadu > Current socio-economic issues > Current socio-economic issues",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > History of Tamil Society > Origin of the Tamils",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > History of Tamil Society > Sangam Age Three Dynasties (Chera, Chola, Pandya)",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > History of Tamil Society > Sangam Age Tamil Cities",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > archaeological discoveries > Excavated Sites by Tamil Nadu Archaeology Department",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > archaeological discoveries > Non-Tamil Language References",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > archaeological discoveries > Accounts of Foreigners",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Tamil literature > Eight Anthologies (Ettuthokai)",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Tamil literature > Ten Idylls (Pathuppattu)",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Tamil literature > Eighteen Minor Works (Pathinen Keezhkanakku Noolgal)",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Tamil literature > Five Great Epics (Aimperum Kappiyangal)",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Tamil literature > Five Small Epics (Ainchiru Kappiyangal)",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Tamil literature > Continuity Poems (Thodarnilai Seiyyulgal)",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Tamil literature > Bhakti Literature",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Thirukkural > Secular / Non-Religious Literature",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Thirukkural > Impact of Thirukkural on Humanity",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Thirukkural > Relation to Everyday Life",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Thirukkural > Thirukkural and Timeless Values - Humanism, Equality",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Thirukkural > Philosophical Doctrines in Thirukkural",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Thirukkural > Thirukkural in Social, Political, and Economic Events",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Early agitations aginst British Rule > Nayak Rule in Tamil Nadu",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Early agitations aginst British Rule > Puli Thevar",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Early agitations aginst British Rule > Veerapandiya Kattabomman",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Early agitations aginst British Rule > Maruthu Brothers",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Early agitations aginst British Rule > South Indian Confederacy for Liberation",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Early agitations aginst British Rule > Vellore Revolt",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Role of Tamil Nadu in freedom struggle > Madras Native Association",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Role of Tamil Nadu in freedom struggle > Madras Mahajana Sabha",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Role of Tamil Nadu in freedom struggle > Swadeshi Steam Navigation Company",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Role of Tamil Nadu in freedom struggle > Madras Jana Sangam",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Role of Tamil Nadu in freedom struggle > Home Rule Movement",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Role of Tamil Nadu in freedom struggle > Rowlatt Satyagraha",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Role of Tamil Nadu in freedom struggle > Khilafat Movement",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Role of Tamil Nadu in freedom struggle > Non-Cooperation Movement",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Role of Tamil Nadu in freedom struggle > Neel Statue Satyagraha",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Role of Tamil Nadu in freedom struggle > Simon Commission Boycott",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Role of Tamil Nadu in freedom struggle > Civil Disobedience Movement",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Role of Tamil Nadu in freedom struggle > Individual Satyagraha",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Role of Tamil Nadu in freedom struggle > Quit India Movement",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Role of women in freedom struggle > Dilliayadi Valliammal",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Role of women in freedom struggle > Anjalai Ammal",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Role of women in freedom struggle > Ambujathammal",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Role of women in freedom struggle > Dr.Muthulakshmi Reddy",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Role of women in freedom struggle > S. Dharmambal",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Role of women in freedom struggle > Moovalur Ramamirtham Ammaiyar",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Role of women in freedom struggle > Rukmani Lakshmipathi",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Role of women in freedom struggle > S. R. Kannamma",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Role of women in freedom struggle > Nagammaiyar",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Role of women in freedom struggle > Durgabai Deshmukh",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Evolution of 19th and 20th century socio-political movements in Tamil Nadu > Ramalinga Adigal (Vallalar)",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Evolution of 19th and 20th century socio-political movements in Tamil Nadu > Narayana Guru",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Evolution of 19th and 20th century socio-political movements in Tamil Nadu > Ayyankali",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Evolution of 19th and 20th century socio-political movements in Tamil Nadu > Vaikunda Swamigal",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Justice Party > Dravidian Association",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Justice Party > South Indian Welfare Rights Association",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Justice Party > Non-Brahmin Conference",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Justice Party > Policies of the Justice Party",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Justice Party > Madras Provincial Association",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Justice Party > Justice Party and the Home Rule Movement",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Justice Party > Justice Party Administration",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Justice Party > Achievers (Reformists & Leaders)",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Self Respect Movement > Fifteen-Point Programme",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Self Respect Movement > Self-Respect Movement Conferences",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Self Respect Movement > Achievements of the Self-Respect Movement",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Dravidian Movement > Rationalism, Social Reform & Dravidian Movement",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Contributions of Thanthai Periyar > Rationalism - Explanation",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Contributions of Thanthai Periyar > Women’s Liberation",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Contributions of Thanthai Periyar > Social Reform",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Contributions of Thanthai Periyar > Vaikom Struggle",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Contributions of Perarignar Anna > Annadurai’s Golden Sayings",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Contributions of Perarignar Anna > Dravidar Kazhagam (DK)",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Contributions of Perarignar Anna > Founding of Dravida Munnetra Kazhagam (DMK)",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Contributions of Perarignar Anna > Achievements of Annadurai as Chief Minister of Tamil Nadu",
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Contributions of Perarignar Anna > Annadurai’s Literary Works",
    "Aptitude > Simplification > BODMAS",
    "Aptitude > Simplification > Powers",
    "Aptitude > Simplification > Surds & Indices",
    "Aptitude > Simplification > AP & GP",
    "Aptitude > Simplification > Special Series",
    "Aptitude > Percentage > Percentage Increase and Decrease",
    "Aptitude > Percentage > Exam and Marks Related Problems",
    "Aptitude > Percentage > Population and Growth Problems",
    "Aptitude > Percentage > Profit and Loss",
    "Aptitude > Highest Common Factor (HCF) > Problems on Remainders",
    "Aptitude > Lowest Common Multiple (LCM) > problems on Multiples and Factors",
    "Aptitude > Lowest Common Multiple (LCM) > Prime Factorization and Division Method Usage",
    "Aptitude > Ratio and Proportion > Mixture and Alligation",
    "Aptitude > Ratio and Proportion > Problems on Ages",
    "Aptitude > Ratio and Proportion > Number System",
    "Aptitude > Ratio and Proportion > Average",
    "Aptitude > Simple interest > Finding Total Amount, Principal, Interest, Time",
    "Aptitude > Simple interest > Borrowing and Lending Problem",
    "Aptitude > Compound interest > Finding Total Amount, Principal, Interest, Time",
    "Aptitude > Compound interest > Compound Interest When Interest is Compounded Half-Yearly or Quarterly",
    "Aptitude > Compound interest > Difference Between Simple Interest and Compound Interest",
    "Aptitude > Area > Square",
    "Aptitude > Area > Rectangle",
    "Aptitude > Area > Triangle",
    "Aptitude > Area > Circle",
    "Aptitude > Area > Parallelogram",
    "Aptitude > Area > Trapezoid",
    "Aptitude > Volume > Cube",
    "Aptitude > Volume > Cuboid",
    "Aptitude > Volume > Cone",
    "Aptitude > Volume > Cylinder",
    "Aptitude > Volume > Sphere",
    "Aptitude > Volume > Hemi Sphere",
    "Aptitude > Time and Work > Work Done by Multiple People Together",
    "Aptitude > Time and Work > Work and Efficiency Relationship",
    "Aptitude > Time and Work > Work Done by Alternating Workers",
    "Reasoning > Logical reasoning > seating arrangment",
    "Reasoning > Logical reasoning > Chronological order",
    "Reasoning > Logical reasoning > syllogism",
    "Reasoning > Logical reasoning > Venn diagram",
    "Reasoning > Logical reasoning > Calander",
    "Reasoning > Logical reasoning > Statement and Conclusions",
    "Reasoning > Puzzles > Box Type Missing numbers",
    "Reasoning > Puzzles > Number of Triangle Etc",
    "Reasoning > Puzzles > Blood Relations",
    "Reasoning > Puzzles > Classification & Odd one out",
    "Reasoning > Dice > Normal Dice",
    "Reasoning > Dice > Standard Dice",
    "Reasoning > Visual reasoning > Clock",
    "Reasoning > Visual reasoning > Directions",
    "Reasoning > Visual reasoning > Embeded figures",
    "Reasoning > Visual reasoning > Figural Classifications",
    "Reasoning > Visual reasoning > Paper Cutting and Folding",
    "Reasoning > Visual reasoning > Mirror iamge",
    "Reasoning > Alpha numeric reasoning > Analogy",
    "Reasoning > Alpha numeric reasoning > Coding and decoding",
    "Reasoning > Alpha numeric reasoning > Missing Letters",
    "Reasoning > Number series > Mathamatical Operations",
    "Reasoning > Number series > Missing numbers",
    "Reasoning > Number series > Series complete",
]

TNPSC_TRIPLET_DICT: Dict[str, Dict[str, str]] = {
    "General Science > Physics > Nature of Universe": {
        "subject": "General Science",
        "topic": "Physics",
        "subtopic": "Nature of Universe"
    },
    "General Science > Physics > General Scientific laws": {
        "subject": "General Science",
        "topic": "Physics",
        "subtopic": "General Scientific laws"
    },
    "General Science > Physics - Mechanics > Force": {
        "subject": "General Science",
        "topic": "Physics - Mechanics",
        "subtopic": "Force"
    },
    "General Science > Physics - Mechanics > Motion": {
        "subject": "General Science",
        "topic": "Physics - Mechanics",
        "subtopic": "Motion"
    },
    "General Science > Physics - Mechanics > Energy": {
        "subject": "General Science",
        "topic": "Physics - Mechanics",
        "subtopic": "Energy"
    },
    "General Science > Physics - Application > Light": {
        "subject": "General Science",
        "topic": "Physics - Application",
        "subtopic": "Light"
    },
    "General Science > Physics - Application > Sound": {
        "subject": "General Science",
        "topic": "Physics - Application",
        "subtopic": "Sound"
    },
    "General Science > Physics - Application > Heat": {
        "subject": "General Science",
        "topic": "Physics - Application",
        "subtopic": "Heat"
    },
    "General Science > Physics - Application > Electricity and Magnetism": {
        "subject": "General Science",
        "topic": "Physics - Application",
        "subtopic": "Electricity and Magnetism"
    },
    "General Science > Physics - Application > Nuclear Physics": {
        "subject": "General Science",
        "topic": "Physics - Application",
        "subtopic": "Nuclear Physics"
    },
    "General Science > Physics - Application > Laser": {
        "subject": "General Science",
        "topic": "Physics - Application",
        "subtopic": "Laser"
    },
    "General Science > Physics - Application > Electronics and Communications": {
        "subject": "General Science",
        "topic": "Physics - Application",
        "subtopic": "Electronics and Communications"
    },
    "General Science > Physics - Application > Properties of matter": {
        "subject": "General Science",
        "topic": "Physics - Application",
        "subtopic": "Properties of matter"
    },
    "General Science > Chemistry > Elements": {
        "subject": "General Science",
        "topic": "Chemistry",
        "subtopic": "Elements"
    },
    "General Science > Chemistry > Compounds": {
        "subject": "General Science",
        "topic": "Chemistry",
        "subtopic": "Compounds"
    },
    "General Science > Chemistry > Acids, Bases & Salts": {
        "subject": "General Science",
        "topic": "Chemistry",
        "subtopic": "Acids, Bases & Salts"
    },
    "General Science > Chemistry > Petroleum Products": {
        "subject": "General Science",
        "topic": "Chemistry",
        "subtopic": "Petroleum Products"
    },
    "General Science > Chemistry > fertilizers, pesticides": {
        "subject": "General Science",
        "topic": "Chemistry",
        "subtopic": "fertilizers, pesticides"
    },
    "General Science > Biology > Main concepts of Life Science": {
        "subject": "General Science",
        "topic": "Biology",
        "subtopic": "Main concepts of Life Science"
    },
    "General Science > Biology > Classification of Living Organisms": {
        "subject": "General Science",
        "topic": "Biology",
        "subtopic": "Classification of Living Organisms"
    },
    "General Science > Biology > Evolution": {
        "subject": "General Science",
        "topic": "Biology",
        "subtopic": "Evolution"
    },
    "General Science > Biology > Genetics": {
        "subject": "General Science",
        "topic": "Biology",
        "subtopic": "Genetics"
    },
    "General Science > Biology > Physiology": {
        "subject": "General Science",
        "topic": "Biology",
        "subtopic": "Physiology"
    },
    "General Science > Biology > Nutrition": {
        "subject": "General Science",
        "topic": "Biology",
        "subtopic": "Nutrition"
    },
    "General Science > Biology > Health and Hygiene": {
        "subject": "General Science",
        "topic": "Biology",
        "subtopic": "Health and Hygiene"
    },
    "General Science > Biology > Human Diseases": {
        "subject": "General Science",
        "topic": "Biology",
        "subtopic": "Human Diseases"
    },
    "General Science > Environment > Environment and ecology": {
        "subject": "General Science",
        "topic": "Environment",
        "subtopic": "Environment and ecology"
    },
    "General Science > Latest Inventions in science and technology > Latest inventions in science and technology": {
        "subject": "General Science",
        "topic": "Latest Inventions in science and technology",
        "subtopic": "Latest inventions in science and technology"
    },
    "General Science > Miscellaneous > Miscellaneous": {
        "subject": "General Science",
        "topic": "Miscellaneous",
        "subtopic": "Miscellaneous"
    },
    "General Science > Current Affairs > Current Affairs": {
        "subject": "General Science",
        "topic": "Current Affairs",
        "subtopic": "Current Affairs"
    },
    "Geography of India > Location and physiography of India > India: An Introduction": {
        "subject": "Geography of India",
        "topic": "Location and physiography of India",
        "subtopic": "India: An Introduction"
    },
    "Geography of India > Location and physiography of India > The Himalayas": {
        "subject": "Geography of India",
        "topic": "Location and physiography of India",
        "subtopic": "The Himalayas"
    },
    "Geography of India > Location and physiography of India > Indo Gangetic plain": {
        "subject": "Geography of India",
        "topic": "Location and physiography of India",
        "subtopic": "Indo Gangetic plain"
    },
    "Geography of India > Location and physiography of India > Peninsular plateau": {
        "subject": "Geography of India",
        "topic": "Location and physiography of India",
        "subtopic": "Peninsular plateau"
    },
    "Geography of India > Location and physiography of India > Thar desert": {
        "subject": "Geography of India",
        "topic": "Location and physiography of India",
        "subtopic": "Thar desert"
    },
    "Geography of India > Location and physiography of India > Coastal plains": {
        "subject": "Geography of India",
        "topic": "Location and physiography of India",
        "subtopic": "Coastal plains"
    },
    "Geography of India > Location and physiography of India > The islands": {
        "subject": "Geography of India",
        "topic": "Location and physiography of India",
        "subtopic": "The islands"
    },
    "Geography of India > Drainage system > Himalayan Rivers": {
        "subject": "Geography of India",
        "topic": "Drainage system",
        "subtopic": "Himalayan Rivers"
    },
    "Geography of India > Drainage system > Peninsular Rivers": {
        "subject": "Geography of India",
        "topic": "Drainage system",
        "subtopic": "Peninsular Rivers"
    },
    "Geography of India > Drainage system > Lakes- types and lakes in India": {
        "subject": "Geography of India",
        "topic": "Drainage system",
        "subtopic": "Lakes- types and lakes in India"
    },
    "Geography of India > Drainage system > Dams and waterfals": {
        "subject": "Geography of India",
        "topic": "Drainage system",
        "subtopic": "Dams and waterfals"
    },
    "Geography of India > Climate of India > Composition of the Atmosphere": {
        "subject": "Geography of India",
        "topic": "Climate of India",
        "subtopic": "Composition of the Atmosphere"
    },
    "Geography of India > Climate of India > Layers of the Atmosphere": {
        "subject": "Geography of India",
        "topic": "Climate of India",
        "subtopic": "Layers of the Atmosphere"
    },
    "Geography of India > Climate of India > Heat Zones of the World": {
        "subject": "Geography of India",
        "topic": "Climate of India",
        "subtopic": "Heat Zones of the World"
    },
    "Geography of India > Climate of India > The factors affecting the climate": {
        "subject": "Geography of India",
        "topic": "Climate of India",
        "subtopic": "The factors affecting the climate"
    },
    "Geography of India > Climate of India > Indian Monsoon": {
        "subject": "Geography of India",
        "topic": "Climate of India",
        "subtopic": "Indian Monsoon"
    },
    "Geography of India > Natural Vegetation > Classification of forest": {
        "subject": "Geography of India",
        "topic": "Natural Vegetation",
        "subtopic": "Classification of forest"
    },
    "Geography of India > Natural Vegetation > Indian State of Forest Report": {
        "subject": "Geography of India",
        "topic": "Natural Vegetation",
        "subtopic": "Indian State of Forest Report"
    },
    "Geography of India > Natural Vegetation > Biodiversity hotspots in India": {
        "subject": "Geography of India",
        "topic": "Natural Vegetation",
        "subtopic": "Biodiversity hotspots in India"
    },
    "Geography of India > Natural Vegetation > Major Threats to Biodiversity": {
        "subject": "Geography of India",
        "topic": "Natural Vegetation",
        "subtopic": "Major Threats to Biodiversity"
    },
    "Geography of India > Natural Vegetation > The Protected Areas of India": {
        "subject": "Geography of India",
        "topic": "Natural Vegetation",
        "subtopic": "The Protected Areas of India"
    },
    "Geography of India > Natural Vegetation > Specialised projects in India": {
        "subject": "Geography of India",
        "topic": "Natural Vegetation",
        "subtopic": "Specialised projects in India"
    },
    "Geography of India > Agricultural and Soils > Soils of India": {
        "subject": "Geography of India",
        "topic": "Agricultural and Soils",
        "subtopic": "Soils of India"
    },
    "Geography of India > Agricultural and Soils > Irrigation": {
        "subject": "Geography of India",
        "topic": "Agricultural and Soils",
        "subtopic": "Irrigation"
    },
    "Geography of India > Agricultural and Soils > Agriculture IN INDIA": {
        "subject": "Geography of India",
        "topic": "Agricultural and Soils",
        "subtopic": "Agriculture IN INDIA"
    },
    "Geography of India > Agricultural and Soils > Livestock & Fisheries": {
        "subject": "Geography of India",
        "topic": "Agricultural and Soils",
        "subtopic": "Livestock & Fisheries"
    },
    "Geography of India > Minerals and Natural Resources > Classification of Resources": {
        "subject": "Geography of India",
        "topic": "Minerals and Natural Resources",
        "subtopic": "Classification of Resources"
    },
    "Geography of India > Minerals and Natural Resources > Types of minerals": {
        "subject": "Geography of India",
        "topic": "Minerals and Natural Resources",
        "subtopic": "Types of minerals"
    },
    "Geography of India > Minerals and Natural Resources > Industries": {
        "subject": "Geography of India",
        "topic": "Minerals and Natural Resources",
        "subtopic": "Industries"
    },
    "Geography of India > Transport - Communication > Road transport": {
        "subject": "Geography of India",
        "topic": "Transport - Communication",
        "subtopic": "Road transport"
    },
    "Geography of India > Transport - Communication > Railways": {
        "subject": "Geography of India",
        "topic": "Transport - Communication",
        "subtopic": "Railways"
    },
    "Geography of India > Transport - Communication > Water transport, ports": {
        "subject": "Geography of India",
        "topic": "Transport - Communication",
        "subtopic": "Water transport, ports"
    },
    "Geography of India > Transport - Communication > Air transport": {
        "subject": "Geography of India",
        "topic": "Transport - Communication",
        "subtopic": "Air transport"
    },
    "Geography of India > Transport - Communication > International trade routes": {
        "subject": "Geography of India",
        "topic": "Transport - Communication",
        "subtopic": "International trade routes"
    },
    "Geography of India > Transport - Communication > Communication": {
        "subject": "Geography of India",
        "topic": "Transport - Communication",
        "subtopic": "Communication"
    },
    "Geography of India > Social Geography > Population density and distribution": {
        "subject": "Geography of India",
        "topic": "Social Geography",
        "subtopic": "Population density and distribution"
    },
    "Geography of India > Social Geography > Urbanization": {
        "subject": "Geography of India",
        "topic": "Social Geography",
        "subtopic": "Urbanization"
    },
    "Geography of India > Racial, Linguistic Groups and Major Tribes > Racial Groups": {
        "subject": "Geography of India",
        "topic": "Racial, Linguistic Groups and Major Tribes",
        "subtopic": "Racial Groups"
    },
    "Geography of India > Racial, Linguistic Groups and Major Tribes > Religion": {
        "subject": "Geography of India",
        "topic": "Racial, Linguistic Groups and Major Tribes",
        "subtopic": "Religion"
    },
    "Geography of India > Racial, Linguistic Groups and Major Tribes > Tribal Distribution in world": {
        "subject": "Geography of India",
        "topic": "Racial, Linguistic Groups and Major Tribes",
        "subtopic": "Tribal Distribution in world"
    },
    "Geography of India > Racial, Linguistic Groups and Major Tribes > Tribal in India": {
        "subject": "Geography of India",
        "topic": "Racial, Linguistic Groups and Major Tribes",
        "subtopic": "Tribal in India"
    },
    "Geography of India > Racial, Linguistic Groups and Major Tribes > Tribals in Tamilnadu": {
        "subject": "Geography of India",
        "topic": "Racial, Linguistic Groups and Major Tribes",
        "subtopic": "Tribals in Tamilnadu"
    },
    "Geography of India > Racial, Linguistic Groups and Major Tribes > Linguistic Groups": {
        "subject": "Geography of India",
        "topic": "Racial, Linguistic Groups and Major Tribes",
        "subtopic": "Linguistic Groups"
    },
    "Geography of India > Natural calamity - Disaster Management > Natural disasters": {
        "subject": "Geography of India",
        "topic": "Natural calamity - Disaster Management",
        "subtopic": "Natural disasters"
    },
    "Geography of India > Natural calamity - Disaster Management > Man-made disasters": {
        "subject": "Geography of India",
        "topic": "Natural calamity - Disaster Management",
        "subtopic": "Man-made disasters"
    },
    "Geography of India > Natural calamity - Disaster Management > National Disaster Management Authority": {
        "subject": "Geography of India",
        "topic": "Natural calamity - Disaster Management",
        "subtopic": "National Disaster Management Authority"
    },
    "Geography of India > Environmental pollution > Pollution": {
        "subject": "Geography of India",
        "topic": "Environmental pollution",
        "subtopic": "Pollution"
    },
    "Geography of India > Environmental pollution > Pollutants": {
        "subject": "Geography of India",
        "topic": "Environmental pollution",
        "subtopic": "Pollutants"
    },
    "Geography of India > Environmental pollution > Classification of Pollutants": {
        "subject": "Geography of India",
        "topic": "Environmental pollution",
        "subtopic": "Classification of Pollutants"
    },
    "Geography of India > Environmental pollution > Types of Pollution": {
        "subject": "Geography of India",
        "topic": "Environmental pollution",
        "subtopic": "Types of Pollution"
    },
    "Geography of India > Environmental pollution > Government Initiatives to Combat Pollution": {
        "subject": "Geography of India",
        "topic": "Environmental pollution",
        "subtopic": "Government Initiatives to Combat Pollution"
    },
    "Geography of India > Climate Change > Factors Affecting Climate Change": {
        "subject": "Geography of India",
        "topic": "Climate Change",
        "subtopic": "Factors Affecting Climate Change"
    },
    "Geography of India > Climate Change > Evidence for Rapid Climate Change in India": {
        "subject": "Geography of India",
        "topic": "Climate Change",
        "subtopic": "Evidence for Rapid Climate Change in India"
    },
    "Geography of India > Climate Change > Effects of climate change in India": {
        "subject": "Geography of India",
        "topic": "Climate Change",
        "subtopic": "Effects of climate change in India"
    },
    "Geography of India > Climate Change > India’s response to Climate Change": {
        "subject": "Geography of India",
        "topic": "Climate Change",
        "subtopic": "India’s response to Climate Change"
    },
    "Geography of India > Green energy > Solar Power, Wind Power, Hydropower, Geothermal Energy, Biomass, Biofuels": {
        "subject": "Geography of India",
        "topic": "Green energy",
        "subtopic": "Solar Power, Wind Power, Hydropower, Geothermal Energy, Biomass, Biofuels"
    },
    "Geography of India > Green energy > Renewable Energy Potential States in India": {
        "subject": "Geography of India",
        "topic": "Green energy",
        "subtopic": "Renewable Energy Potential States in India"
    },
    "Geography of India > Green energy > Achievements of India in the Renewable energy sector": {
        "subject": "Geography of India",
        "topic": "Green energy",
        "subtopic": "Achievements of India in the Renewable energy sector"
    },
    "History, Culture of India and Indian National Movement > Indus Valley Civilization > Phases of IVC": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indus Valley Civilization",
        "subtopic": "Phases of IVC"
    },
    "History, Culture of India and Indian National Movement > Indus Valley Civilization > Lifestyle of people during IVC": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indus Valley Civilization",
        "subtopic": "Lifestyle of people during IVC"
    },
    "History, Culture of India and Indian National Movement > Indus Valley Civilization > Findings, sites ,  economic activities": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indus Valley Civilization",
        "subtopic": "Findings, sites ,  economic activities"
    },
    "History, Culture of India and Indian National Movement > Gupta Period > Sources of Gupta Rule": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Gupta Period",
        "subtopic": "Sources of Gupta Rule"
    },
    "History, Culture of India and Indian National Movement > Gupta Period > Important rulers and titles adopted by Gupta kings": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Gupta Period",
        "subtopic": "Important rulers and titles adopted by Gupta kings"
    },
    "History, Culture of India and Indian National Movement > Gupta Period > Foreign Travellers Visit - Fahien’s Visit": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Gupta Period",
        "subtopic": "Foreign Travellers Visit - Fahien’s Visit"
    },
    "History, Culture of India and Indian National Movement > Gupta Period > Life under Guptas": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Gupta Period",
        "subtopic": "Life under Guptas"
    },
    "History, Culture of India and Indian National Movement > Gupta Period > Post Guptas": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Gupta Period",
        "subtopic": "Post Guptas"
    },
    "History, Culture of India and Indian National Movement > Delhi Sultanate > Early Muslim Invasions": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Delhi Sultanate",
        "subtopic": "Early Muslim Invasions"
    },
    "History, Culture of India and Indian National Movement > Delhi Sultanate > Major Dynasties and their rulers": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Delhi Sultanate",
        "subtopic": "Major Dynasties and their rulers"
    },
    "History, Culture of India and Indian National Movement > Delhi Sultanate > Life under Delhi Sultanate": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Delhi Sultanate",
        "subtopic": "Life under Delhi Sultanate"
    },
    "History, Culture of India and Indian National Movement > Mughals > Establishment of Mughal Empire": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Mughals",
        "subtopic": "Establishment of Mughal Empire"
    },
    "History, Culture of India and Indian National Movement > Mughals > Akbar": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Mughals",
        "subtopic": "Akbar"
    },
    "History, Culture of India and Indian National Movement > Mughals > Jahangir and Shah Jahan": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Mughals",
        "subtopic": "Jahangir and Shah Jahan"
    },
    "History, Culture of India and Indian National Movement > Mughals > Aurangzeb": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Mughals",
        "subtopic": "Aurangzeb"
    },
    "History, Culture of India and Indian National Movement > Mughals > Life under Mughals": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Mughals",
        "subtopic": "Life under Mughals"
    },
    "History, Culture of India and Indian National Movement > Mughals > Mughals Contribution": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Mughals",
        "subtopic": "Mughals Contribution"
    },
    "History, Culture of India and Indian National Movement > Marathas > Rise of Marathas under Shivaji": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Marathas",
        "subtopic": "Rise of Marathas under Shivaji"
    },
    "History, Culture of India and Indian National Movement > Marathas > Treaty of Purandar": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Marathas",
        "subtopic": "Treaty of Purandar"
    },
    "History, Culture of India and Indian National Movement > Marathas > Sambhaji": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Marathas",
        "subtopic": "Sambhaji"
    },
    "History, Culture of India and Indian National Movement > Marathas > Rajaram": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Marathas",
        "subtopic": "Rajaram"
    },
    "History, Culture of India and Indian National Movement > Marathas > Shahu": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Marathas",
        "subtopic": "Shahu"
    },
    "History, Culture of India and Indian National Movement > Marathas > Peshwas under Maratha empire": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Marathas",
        "subtopic": "Peshwas under Maratha empire"
    },
    "History, Culture of India and Indian National Movement > Marathas > Mughals and Marathas conflicts": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Marathas",
        "subtopic": "Mughals and Marathas conflicts"
    },
    "History, Culture of India and Indian National Movement > Marathas > Anglo-Maratha Wars": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Marathas",
        "subtopic": "Anglo-Maratha Wars"
    },
    "History, Culture of India and Indian National Movement > Marathas > Decline of Marathas": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Marathas",
        "subtopic": "Decline of Marathas"
    },
    "History, Culture of India and Indian National Movement > Vijaynagar empire > Dynasties": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Vijaynagar empire",
        "subtopic": "Dynasties"
    },
    "History, Culture of India and Indian National Movement > Vijaynagar empire > Administration": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Vijaynagar empire",
        "subtopic": "Administration"
    },
    "History, Culture of India and Indian National Movement > Vijaynagar empire > Army and military organisation": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Vijaynagar empire",
        "subtopic": "Army and military organisation"
    },
    "History, Culture of India and Indian National Movement > Vijaynagar empire > Social and economic life": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Vijaynagar empire",
        "subtopic": "Social and economic life"
    },
    "History, Culture of India and Indian National Movement > Vijaynagar empire > Social life": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Vijaynagar empire",
        "subtopic": "Social life"
    },
    "History, Culture of India and Indian National Movement > The Bahmani Kingdom > Rulers of the Bahmani Kingdom": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "The Bahmani Kingdom",
        "subtopic": "Rulers of the Bahmani Kingdom"
    },
    "History, Culture of India and Indian National Movement > The Bahmani Kingdom > The Five Kingdoms": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "The Bahmani Kingdom",
        "subtopic": "The Five Kingdoms"
    },
    "History, Culture of India and Indian National Movement > The Bahmani Kingdom > Administration": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "The Bahmani Kingdom",
        "subtopic": "Administration"
    },
    "History, Culture of India and Indian National Movement > The Bahmani Kingdom > Contribution to Education": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "The Bahmani Kingdom",
        "subtopic": "Contribution to Education"
    },
    "History, Culture of India and Indian National Movement > The Bahmani Kingdom > Art and Architecture": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "The Bahmani Kingdom",
        "subtopic": "Art and Architecture"
    },
    "History, Culture of India and Indian National Movement > The Bahmani Kingdom > Decline of Bahmani Kingdom": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "The Bahmani Kingdom",
        "subtopic": "Decline of Bahmani Kingdom"
    },
    "History, Culture of India and Indian National Movement > South Indian History > Sangam Age": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "South Indian History",
        "subtopic": "Sangam Age"
    },
    "History, Culture of India and Indian National Movement > South Indian History > Life under Sangam Age": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "South Indian History",
        "subtopic": "Life under Sangam Age"
    },
    "History, Culture of India and Indian National Movement > South Indian History > Kalabras": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "South Indian History",
        "subtopic": "Kalabras"
    },
    "History, Culture of India and Indian National Movement > South Indian History > Pallavas dynasty": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "South Indian History",
        "subtopic": "Pallavas dynasty"
    },
    "History, Culture of India and Indian National Movement > South Indian History > Chalukya Dynasty": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "South Indian History",
        "subtopic": "Chalukya Dynasty"
    },
    "History, Culture of India and Indian National Movement > South Indian History > Rashtrakutas Dynasty": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "South Indian History",
        "subtopic": "Rashtrakutas Dynasty"
    },
    "History, Culture of India and Indian National Movement > South Indian History > Later Pandyas": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "South Indian History",
        "subtopic": "Later Pandyas"
    },
    "History, Culture of India and Indian National Movement > South Indian History > Later Cholas": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "South Indian History",
        "subtopic": "Later Cholas"
    },
    "History, Culture of India and Indian National Movement > Religious development in Medieval India > Sufism": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Religious development in Medieval India",
        "subtopic": "Sufism"
    },
    "History, Culture of India and Indian National Movement > Religious development in Medieval India > Bhaktism": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Religious development in Medieval India",
        "subtopic": "Bhaktism"
    },
    "History, Culture of India and Indian National Movement > Religious development in Medieval India > Sikhism": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Religious development in Medieval India",
        "subtopic": "Sikhism"
    },
    "History, Culture of India and Indian National Movement > Cultural History of India > Art and Culture": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Cultural History of India",
        "subtopic": "Art and Culture"
    },
    "History, Culture of India and Indian National Movement > Cultural History of India > Characteristics of Indian Culture": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Cultural History of India",
        "subtopic": "Characteristics of Indian Culture"
    },
    "History, Culture of India and Indian National Movement > Cultural History of India > India as a Secular State": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Cultural History of India",
        "subtopic": "India as a Secular State"
    },
    "History, Culture of India and Indian National Movement > Cultural History of India > Social Harmony": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Cultural History of India",
        "subtopic": "Social Harmony"
    },
    "History, Culture of India and Indian National Movement > Ancient India > Vedic Age": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Ancient India",
        "subtopic": "Vedic Age"
    },
    "History, Culture of India and Indian National Movement > Ancient India > Pre Mauryan Age": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Ancient India",
        "subtopic": "Pre Mauryan Age"
    },
    "History, Culture of India and Indian National Movement > Ancient India > Mauryan Age": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Ancient India",
        "subtopic": "Mauryan Age"
    },
    "History, Culture of India and Indian National Movement > Ancient India > Post Mauryan Age": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Ancient India",
        "subtopic": "Post Mauryan Age"
    },
    "History, Culture of India and Indian National Movement > Ancient India > Foreign successors of Mauryas": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Ancient India",
        "subtopic": "Foreign successors of Mauryas"
    },
    "History, Culture of India and Indian National Movement > Advent of Europeans in India > The Portuguese in India": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Advent of Europeans in India",
        "subtopic": "The Portuguese in India"
    },
    "History, Culture of India and Indian National Movement > Advent of Europeans in India > The Dutch in India": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Advent of Europeans in India",
        "subtopic": "The Dutch in India"
    },
    "History, Culture of India and Indian National Movement > Advent of Europeans in India > The Danes in India": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Advent of Europeans in India",
        "subtopic": "The Danes in India"
    },
    "History, Culture of India and Indian National Movement > Advent of Europeans in India > The English": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Advent of Europeans in India",
        "subtopic": "The English"
    },
    "History, Culture of India and Indian National Movement > Advent of Europeans in India > The French": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Advent of Europeans in India",
        "subtopic": "The French"
    },
    "History, Culture of India and Indian National Movement > Advent of Europeans in India > Carnatic Wars": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Advent of Europeans in India",
        "subtopic": "Carnatic Wars"
    },
    "History, Culture of India and Indian National Movement > Advent of Europeans in India > British Expansion In India": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Advent of Europeans in India",
        "subtopic": "British Expansion In India"
    },
    "History, Culture of India and Indian National Movement > Advent of Europeans in India > Economic Policies of British": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Advent of Europeans in India",
        "subtopic": "Economic Policies of British"
    },
    "History, Culture of India and Indian National Movement > Advent of Europeans in India > Impact of British Administration": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Advent of Europeans in India",
        "subtopic": "Impact of British Administration"
    },
    "History, Culture of India and Indian National Movement > Early uprising against British rule > Tribal Movements": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Early uprising against British rule",
        "subtopic": "Tribal Movements"
    },
    "History, Culture of India and Indian National Movement > Early uprising against British rule > Peasant Movements": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Early uprising against British rule",
        "subtopic": "Peasant Movements"
    },
    "History, Culture of India and Indian National Movement > Early uprising against British rule > Politico- religious movements": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Early uprising against British rule",
        "subtopic": "Politico- religious movements"
    },
    "History, Culture of India and Indian National Movement > The Revolt of 1857 > Causes of the Revolt": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "The Revolt of 1857",
        "subtopic": "Causes of the Revolt"
    },
    "History, Culture of India and Indian National Movement > The Revolt of 1857 > Centres and Spread of the Revolt": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "The Revolt of 1857",
        "subtopic": "Centres and Spread of the Revolt"
    },
    "History, Culture of India and Indian National Movement > The Revolt of 1857 > Leaders of the Revolt": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "The Revolt of 1857",
        "subtopic": "Leaders of the Revolt"
    },
    "History, Culture of India and Indian National Movement > The Revolt of 1857 > Causes of Failure of the Revolt": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "The Revolt of 1857",
        "subtopic": "Causes of Failure of the Revolt"
    },
    "History, Culture of India and Indian National Movement > The Revolt of 1857 > Nature and Impact of the Revolt": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "The Revolt of 1857",
        "subtopic": "Nature and Impact of the Revolt"
    },
    "History, Culture of India and Indian National Movement > National Renaissance Social and religious reform movements > Socio-Religious Reforms": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "National Renaissance Social and religious reform movements",
        "subtopic": "Socio-Religious Reforms"
    },
    "History, Culture of India and Indian National Movement > National Renaissance Social and religious reform movements > Muslim reform movements": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "National Renaissance Social and religious reform movements",
        "subtopic": "Muslim reform movements"
    },
    "History, Culture of India and Indian National Movement > National Renaissance Social and religious reform movements > Miscellaneous movements": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "National Renaissance Social and religious reform movements",
        "subtopic": "Miscellaneous movements"
    },
    "History, Culture of India and Indian National Movement > National Renaissance Social and religious reform movements > PERSONALITIES": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "National Renaissance Social and religious reform movements",
        "subtopic": "PERSONALITIES"
    },
    "History, Culture of India and Indian National Movement > Indian National Congress (1885 - 1920) > Early Phase Indian National Congress": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Congress (1885 - 1920)",
        "subtopic": "Early Phase Indian National Congress"
    },
    "History, Culture of India and Indian National Movement > Indian National Congress (1885 - 1920) > The Moderate Congress (1885-1905)": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Congress (1885 - 1920)",
        "subtopic": "The Moderate Congress (1885-1905)"
    },
    "History, Culture of India and Indian National Movement > Indian National Congress (1885 - 1920) > Political associations in Bengal, Bombay and Madras GoI Act 1861 and 1892": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Congress (1885 - 1920)",
        "subtopic": "Political associations in Bengal, Bombay and Madras GoI Act 1861 and 1892"
    },
    "History, Culture of India and Indian National Movement > Indian National Congress (1885 - 1920) > The Extremist (1905-1920)": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Congress (1885 - 1920)",
        "subtopic": "The Extremist (1905-1920)"
    },
    "History, Culture of India and Indian National Movement > Indian National Congress (1885 - 1920) > Differences between the Moderates and the Extremists": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Congress (1885 - 1920)",
        "subtopic": "Differences between the Moderates and the Extremists"
    },
    "History, Culture of India and Indian National Movement > Indian National Congress (1885 - 1920) > Pre congress campaign": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Congress (1885 - 1920)",
        "subtopic": "Pre congress campaign"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - I (1905-1918) > Partition of Bengal (1905)": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - I (1905-1918)",
        "subtopic": "Partition of Bengal (1905)"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - I (1905-1918) > Swadeshi Movement": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - I (1905-1918)",
        "subtopic": "Swadeshi Movement"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - I (1905-1918) > Muslim League, 1906": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - I (1905-1918)",
        "subtopic": "Muslim League, 1906"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - I (1905-1918) > Surat Session of INC, 1907": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - I (1905-1918)",
        "subtopic": "Surat Session of INC, 1907"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - I (1905-1918) > Indian Council Act (Morley-Minto Act) 1909": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - I (1905-1918)",
        "subtopic": "Indian Council Act (Morley-Minto Act) 1909"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - I (1905-1918) > Ghadar Party, 1913": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - I (1905-1918)",
        "subtopic": "Ghadar Party, 1913"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - I (1905-1918) > Komagata Maru Incident 1914": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - I (1905-1918)",
        "subtopic": "Komagata Maru Incident 1914"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - I (1905-1918) > First world war and its impact": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - I (1905-1918)",
        "subtopic": "First world war and its impact"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - I (1905-1918) > The Lucknow Pact (1916)": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - I (1905-1918)",
        "subtopic": "The Lucknow Pact (1916)"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - II (1918-1929) > Emergence of Gandhi": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - II (1918-1929)",
        "subtopic": "Emergence of Gandhi"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - II (1918-1929) > The Government of India Act, 1919": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - II (1918-1929)",
        "subtopic": "The Government of India Act, 1919"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - II (1918-1929) > Rowlatt Act and Jallianwala Bagh Massacre (1919)": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - II (1918-1929)",
        "subtopic": "Rowlatt Act and Jallianwala Bagh Massacre (1919)"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - II (1918-1929) > Khilafat Movement": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - II (1918-1929)",
        "subtopic": "Khilafat Movement"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - II (1918-1929) > The Non-Cooperation Movement (1920-22)": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - II (1918-1929)",
        "subtopic": "The Non-Cooperation Movement (1920-22)"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - II (1918-1929) > Swarajists and no changers": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - II (1918-1929)",
        "subtopic": "Swarajists and no changers"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - II (1918-1929) > Nagpur Session of Congress": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - II (1918-1929)",
        "subtopic": "Nagpur Session of Congress"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - II (1918-1929) > Swaraj Party and its Evaluation": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - II (1918-1929)",
        "subtopic": "Swaraj Party and its Evaluation"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - II (1918-1929) > Muddiman Committee (1924)": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - II (1918-1929)",
        "subtopic": "Muddiman Committee (1924)"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - II (1918-1929) > Simon Commission (1927)": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - II (1918-1929)",
        "subtopic": "Simon Commission (1927)"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - II (1918-1929) > Bardoli Satyagraha (1928)": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - II (1918-1929)",
        "subtopic": "Bardoli Satyagraha (1928)"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - II (1918-1929) > Nehru Report (1928)": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - II (1918-1929)",
        "subtopic": "Nehru Report (1928)"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - II (1918-1929) > Jinnah’s Fourteen Points": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - II (1918-1929)",
        "subtopic": "Jinnah’s Fourteen Points"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - II (1918-1929) > Calcutta session of INC 1928": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - II (1918-1929)",
        "subtopic": "Calcutta session of INC 1928"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - II (1918-1929) > Delhi Manifesto": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - II (1918-1929)",
        "subtopic": "Delhi Manifesto"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - II (1918-1929) > Lahore Session, 1929": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - II (1918-1929)",
        "subtopic": "Lahore Session, 1929"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - II (1918-1929) > Allahabad Address (1930)": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - II (1918-1929)",
        "subtopic": "Allahabad Address (1930)"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - II (1918-1929) > Emergence of New Forces during 1920s": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - II (1918-1929)",
        "subtopic": "Emergence of New Forces during 1920s"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > Civil Disobedience Movement (1930-1931)": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - III (1930-1947)",
        "subtopic": "Civil Disobedience Movement (1930-1931)"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > Round Table ConferencE": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - III (1930-1947)",
        "subtopic": "Round Table ConferencE"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > Gandhi-Irwin Pact, 1931": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - III (1930-1947)",
        "subtopic": "Gandhi-Irwin Pact, 1931"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > Karachi session of 1931": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - III (1930-1947)",
        "subtopic": "Karachi session of 1931"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > Communal Award": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - III (1930-1947)",
        "subtopic": "Communal Award"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > Poona Pact, 1932": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - III (1930-1947)",
        "subtopic": "Poona Pact, 1932"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > Government of India Act, 1935": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - III (1930-1947)",
        "subtopic": "Government of India Act, 1935"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > World War II and Indian Nationalism": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - III (1930-1947)",
        "subtopic": "World War II and Indian Nationalism"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > Resignation of Congress Ministers (1939)": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - III (1930-1947)",
        "subtopic": "Resignation of Congress Ministers (1939)"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > Poona Resolution and Conditional Support to Britain (1941)": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - III (1930-1947)",
        "subtopic": "Poona Resolution and Conditional Support to Britain (1941)"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > August Offer of 1940": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - III (1930-1947)",
        "subtopic": "August Offer of 1940"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > The Individual Civil Disobedience": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - III (1930-1947)",
        "subtopic": "The Individual Civil Disobedience"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > Two-Nation Theory": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - III (1930-1947)",
        "subtopic": "Two-Nation Theory"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > Demand for Pakistan (1942)": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - III (1930-1947)",
        "subtopic": "Demand for Pakistan (1942)"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > Cripps Mission (1942)": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - III (1930-1947)",
        "subtopic": "Cripps Mission (1942)"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > Quit India Movement": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - III (1930-1947)",
        "subtopic": "Quit India Movement"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > Azad Hind Fauj": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - III (1930-1947)",
        "subtopic": "Azad Hind Fauj"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > Indian National Army": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - III (1930-1947)",
        "subtopic": "Indian National Army"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > I.N.A Trials": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - III (1930-1947)",
        "subtopic": "I.N.A Trials"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > Indian Navy Rebellion": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - III (1930-1947)",
        "subtopic": "Indian Navy Rebellion"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > Rajagopalachari Formula, 1945": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - III (1930-1947)",
        "subtopic": "Rajagopalachari Formula, 1945"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > Desai - Liaqat Pact": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - III (1930-1947)",
        "subtopic": "Desai - Liaqat Pact"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > Cabinet Mission (1946)": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - III (1930-1947)",
        "subtopic": "Cabinet Mission (1946)"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > Wavell Plan": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - III (1930-1947)",
        "subtopic": "Wavell Plan"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > Jinnah’s Direct Action Resolution": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - III (1930-1947)",
        "subtopic": "Jinnah’s Direct Action Resolution"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > Mountbatten Plan of June 1947": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - III (1930-1947)",
        "subtopic": "Mountbatten Plan of June 1947"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > Indian Independence Act 1947": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - III (1930-1947)",
        "subtopic": "Indian Independence Act 1947"
    },
    "History, Culture of India and Indian National Movement > Indian National Movement - III (1930-1947) > Communalism and Partition": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Indian National Movement - III (1930-1947)",
        "subtopic": "Communalism and Partition"
    },
    "History, Culture of India and Indian National Movement > Emergence of Leaders > B.R. Ambedkar": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Emergence of Leaders",
        "subtopic": "B.R. Ambedkar"
    },
    "History, Culture of India and Indian National Movement > Emergence of Leaders > Bhagat Singh": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Emergence of Leaders",
        "subtopic": "Bhagat Singh"
    },
    "History, Culture of India and Indian National Movement > Emergence of Leaders > Bharathiar": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Emergence of Leaders",
        "subtopic": "Bharathiar"
    },
    "History, Culture of India and Indian National Movement > Emergence of Leaders > V.O. Chidambaranar": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Emergence of Leaders",
        "subtopic": "V.O. Chidambaranar"
    },
    "History, Culture of India and Indian National Movement > Emergence of Leaders > Jawaharlal Nehru": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Emergence of Leaders",
        "subtopic": "Jawaharlal Nehru"
    },
    "History, Culture of India and Indian National Movement > Emergence of Leaders > Kamarajar": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Emergence of Leaders",
        "subtopic": "Kamarajar"
    },
    "History, Culture of India and Indian National Movement > Emergence of Leaders > Mahatma Gandhi": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Emergence of Leaders",
        "subtopic": "Mahatma Gandhi"
    },
    "History, Culture of India and Indian National Movement > Emergence of Leaders > Maulana Abul Kalam Azad": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Emergence of Leaders",
        "subtopic": "Maulana Abul Kalam Azad"
    },
    "History, Culture of India and Indian National Movement > Emergence of Leaders > Thanthai Periyar": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Emergence of Leaders",
        "subtopic": "Thanthai Periyar"
    },
    "History, Culture of India and Indian National Movement > Emergence of Leaders > Rajaji": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Emergence of Leaders",
        "subtopic": "Rajaji"
    },
    "History, Culture of India and Indian National Movement > Emergence of Leaders > Subash Chandra Bose": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Emergence of Leaders",
        "subtopic": "Subash Chandra Bose"
    },
    "History, Culture of India and Indian National Movement > Emergence of Leaders > Rabindranath Tagore": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Emergence of Leaders",
        "subtopic": "Rabindranath Tagore"
    },
    "History, Culture of India and Indian National Movement > Emergence of Leaders > Others": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Emergence of Leaders",
        "subtopic": "Others"
    },
    "History, Culture of India and Indian National Movement > Governor Generals During British India > Governor of Bengal (Before 1773)": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Governor Generals During British India",
        "subtopic": "Governor of Bengal (Before 1773)"
    },
    "History, Culture of India and Indian National Movement > Governor Generals During British India > Governor Generals of Bengal (1773-1833)": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Governor Generals During British India",
        "subtopic": "Governor Generals of Bengal (1773-1833)"
    },
    "History, Culture of India and Indian National Movement > Governor Generals During British India > Governor Generals of India (1832-1858)": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Governor Generals During British India",
        "subtopic": "Governor Generals of India (1832-1858)"
    },
    "History, Culture of India and Indian National Movement > Governor Generals During British India > Viceroy of India (1858-1947)": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Governor Generals During British India",
        "subtopic": "Viceroy of India (1858-1947)"
    },
    "History, Culture of India and Indian National Movement > Constitutional Development > Constitutional Development in India": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Constitutional Development",
        "subtopic": "Constitutional Development in India"
    },
    "History, Culture of India and Indian National Movement > Civil Services > Development of Civil Services": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Civil Services",
        "subtopic": "Development of Civil Services"
    },
    "History, Culture of India and Indian National Movement > Education > Development of Education": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Education",
        "subtopic": "Development of Education"
    },
    "History, Culture of India and Indian National Movement > Press > Development of Press": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Press",
        "subtopic": "Development of Press"
    },
    "History, Culture of India and Indian National Movement > Prominent personalities in various spheres > Arts, Science, Literature and Philosophy": {
        "subject": "History, Culture of India and Indian National Movement",
        "topic": "Prominent personalities in various spheres",
        "subtopic": "Arts, Science, Literature and Philosophy"
    },
    "Indian Polity > Evolution of Indian Constitution > Regulating act of 1773": {
        "subject": "Indian Polity",
        "topic": "Evolution of Indian Constitution",
        "subtopic": "Regulating act of 1773"
    },
    "Indian Polity > Evolution of Indian Constitution > Charter Act of 1833": {
        "subject": "Indian Polity",
        "topic": "Evolution of Indian Constitution",
        "subtopic": "Charter Act of 1833"
    },
    "Indian Polity > Evolution of Indian Constitution > Charter Act of 1853": {
        "subject": "Indian Polity",
        "topic": "Evolution of Indian Constitution",
        "subtopic": "Charter Act of 1853"
    },
    "Indian Polity > Evolution of Indian Constitution > Government of India Act of 1858": {
        "subject": "Indian Polity",
        "topic": "Evolution of Indian Constitution",
        "subtopic": "Government of India Act of 1858"
    },
    "Indian Polity > Evolution of Indian Constitution > Indian Councils Act of 1909": {
        "subject": "Indian Polity",
        "topic": "Evolution of Indian Constitution",
        "subtopic": "Indian Councils Act of 1909"
    },
    "Indian Polity > Evolution of Indian Constitution > Government of India Act 1919": {
        "subject": "Indian Polity",
        "topic": "Evolution of Indian Constitution",
        "subtopic": "Government of India Act 1919"
    },
    "Indian Polity > Evolution of Indian Constitution > Government of India Act 1935": {
        "subject": "Indian Polity",
        "topic": "Evolution of Indian Constitution",
        "subtopic": "Government of India Act 1935"
    },
    "Indian Polity > Evolution of Indian Constitution > India Independence Act 1947": {
        "subject": "Indian Polity",
        "topic": "Evolution of Indian Constitution",
        "subtopic": "India Independence Act 1947"
    },
    "Indian Polity > Making of Indian Constiution > Background-Constituent Assembly": {
        "subject": "Indian Polity",
        "topic": "Making of Indian Constiution",
        "subtopic": "Background-Constituent Assembly"
    },
    "Indian Polity > Making of Indian Constiution > Constituent Assembly": {
        "subject": "Indian Polity",
        "topic": "Making of Indian Constiution",
        "subtopic": "Constituent Assembly"
    },
    "Indian Polity > Making of Indian Constiution > Committees (Major & Minor)": {
        "subject": "Indian Polity",
        "topic": "Making of Indian Constiution",
        "subtopic": "Committees (Major & Minor)"
    },
    "Indian Polity > Making of Indian Constiution > Sources of the constitution": {
        "subject": "Indian Polity",
        "topic": "Making of Indian Constiution",
        "subtopic": "Sources of the constitution"
    },
    "Indian Polity > Making of Indian Constiution > Salient features in Indian Constitution": {
        "subject": "Indian Polity",
        "topic": "Making of Indian Constiution",
        "subtopic": "Salient features in Indian Constitution"
    },
    "Indian Polity > Preamble > Nature of Indian State": {
        "subject": "Indian Polity",
        "topic": "Preamble",
        "subtopic": "Nature of Indian State"
    },
    "Indian Polity > Preamble > Objectives of the constitution": {
        "subject": "Indian Polity",
        "topic": "Preamble",
        "subtopic": "Objectives of the constitution"
    },
    "Indian Polity > Preamble > Significance of the Preamble": {
        "subject": "Indian Polity",
        "topic": "Preamble",
        "subtopic": "Significance of the Preamble"
    },
    "Indian Polity > Preamble > Amenability of the Preamble (cases)": {
        "subject": "Indian Polity",
        "topic": "Preamble",
        "subtopic": "Amenability of the Preamble (cases)"
    },
    "Indian Polity > Union, State and Union Territory > Evolution of states and Union territories": {
        "subject": "Indian Polity",
        "topic": "Union, State and Union Territory",
        "subtopic": "Evolution of states and Union territories"
    },
    "Indian Polity > Union, State and Union Territory > Article 1": {
        "subject": "Indian Polity",
        "topic": "Union, State and Union Territory",
        "subtopic": "Article 1"
    },
    "Indian Polity > Union, State and Union Territory > Article 2": {
        "subject": "Indian Polity",
        "topic": "Union, State and Union Territory",
        "subtopic": "Article 2"
    },
    "Indian Polity > Union, State and Union Territory > Article 3": {
        "subject": "Indian Polity",
        "topic": "Union, State and Union Territory",
        "subtopic": "Article 3"
    },
    "Indian Polity > Union, State and Union Territory > Article 4": {
        "subject": "Indian Polity",
        "topic": "Union, State and Union Territory",
        "subtopic": "Article 4"
    },
    "Indian Polity > Union, State and Union Territory > State reorganization commissions": {
        "subject": "Indian Polity",
        "topic": "Union, State and Union Territory",
        "subtopic": "State reorganization commissions"
    },
    "Indian Polity > Citizenship > Article 5 - 11": {
        "subject": "Indian Polity",
        "topic": "Citizenship",
        "subtopic": "Article 5 - 11"
    },
    "Indian Polity > Citizenship > Acquisition of Citizenship": {
        "subject": "Indian Polity",
        "topic": "Citizenship",
        "subtopic": "Acquisition of Citizenship"
    },
    "Indian Polity > Citizenship > Loss of Citizenship": {
        "subject": "Indian Polity",
        "topic": "Citizenship",
        "subtopic": "Loss of Citizenship"
    },
    "Indian Polity > Citizenship > Citizenship Act 1955 and amendments": {
        "subject": "Indian Polity",
        "topic": "Citizenship",
        "subtopic": "Citizenship Act 1955 and amendments"
    },
    "Indian Polity > Fundamental Rights > Right to equality": {
        "subject": "Indian Polity",
        "topic": "Fundamental Rights",
        "subtopic": "Right to equality"
    },
    "Indian Polity > Fundamental Rights > Right to freedom": {
        "subject": "Indian Polity",
        "topic": "Fundamental Rights",
        "subtopic": "Right to freedom"
    },
    "Indian Polity > Fundamental Rights > Right against exploitation": {
        "subject": "Indian Polity",
        "topic": "Fundamental Rights",
        "subtopic": "Right against exploitation"
    },
    "Indian Polity > Fundamental Rights > Right to freedom of Religion": {
        "subject": "Indian Polity",
        "topic": "Fundamental Rights",
        "subtopic": "Right to freedom of Religion"
    },
    "Indian Polity > Fundamental Rights > Cultural and educational rights": {
        "subject": "Indian Polity",
        "topic": "Fundamental Rights",
        "subtopic": "Cultural and educational rights"
    },
    "Indian Polity > Fundamental Rights > Rights to constitutional remedies": {
        "subject": "Indian Polity",
        "topic": "Fundamental Rights",
        "subtopic": "Rights to constitutional remedies"
    },
    "Indian Polity > Fundamental Rights > Impact on fundamental rights": {
        "subject": "Indian Polity",
        "topic": "Fundamental Rights",
        "subtopic": "Impact on fundamental rights"
    },
    "Indian Polity > Directive Principles of State Policy > Socialistic principles": {
        "subject": "Indian Polity",
        "topic": "Directive Principles of State Policy",
        "subtopic": "Socialistic principles"
    },
    "Indian Polity > Directive Principles of State Policy > Gandhian principles": {
        "subject": "Indian Polity",
        "topic": "Directive Principles of State Policy",
        "subtopic": "Gandhian principles"
    },
    "Indian Polity > Directive Principles of State Policy > Liberal - intellectual principles": {
        "subject": "Indian Polity",
        "topic": "Directive Principles of State Policy",
        "subtopic": "Liberal - intellectual principles"
    },
    "Indian Polity > Directive Principles of State Policy > Comparison between DPSP and FRs": {
        "subject": "Indian Polity",
        "topic": "Directive Principles of State Policy",
        "subtopic": "Comparison between DPSP and FRs"
    },
    "Indian Polity > Directive Principles of State Policy > Important Cases related to FR and DPSP": {
        "subject": "Indian Polity",
        "topic": "Directive Principles of State Policy",
        "subtopic": "Important Cases related to FR and DPSP"
    },
    "Indian Polity > Directive Principles of State Policy > Important amendments": {
        "subject": "Indian Polity",
        "topic": "Directive Principles of State Policy",
        "subtopic": "Important amendments"
    },
    "Indian Polity > Fundamental Duties > Committees": {
        "subject": "Indian Polity",
        "topic": "Fundamental Duties",
        "subtopic": "Committees"
    },
    "Indian Polity > Fundamental Duties > Article 51A (List of FDs)": {
        "subject": "Indian Polity",
        "topic": "Fundamental Duties",
        "subtopic": "Article 51A (List of FDs)"
    },
    "Indian Polity > Amendments > Types of amendments": {
        "subject": "Indian Polity",
        "topic": "Amendments",
        "subtopic": "Types of amendments"
    },
    "Indian Polity > Amendments > Emergence of the concept of basic structure": {
        "subject": "Indian Polity",
        "topic": "Amendments",
        "subtopic": "Emergence of the concept of basic structure"
    },
    "Indian Polity > Amendments > Role of judiciary": {
        "subject": "Indian Polity",
        "topic": "Amendments",
        "subtopic": "Role of judiciary"
    },
    "Indian Polity > Union Executive > President": {
        "subject": "Indian Polity",
        "topic": "Union Executive",
        "subtopic": "President"
    },
    "Indian Polity > Union Executive > Vice President": {
        "subject": "Indian Polity",
        "topic": "Union Executive",
        "subtopic": "Vice President"
    },
    "Indian Polity > Union Executive > Prime Minister": {
        "subject": "Indian Polity",
        "topic": "Union Executive",
        "subtopic": "Prime Minister"
    },
    "Indian Polity > Union Executive > Central Council of Ministers": {
        "subject": "Indian Polity",
        "topic": "Union Executive",
        "subtopic": "Central Council of Ministers"
    },
    "Indian Polity > Union Legislature > Rajya Sabha": {
        "subject": "Indian Polity",
        "topic": "Union Legislature",
        "subtopic": "Rajya Sabha"
    },
    "Indian Polity > Union Legislature > Lok Sabha": {
        "subject": "Indian Polity",
        "topic": "Union Legislature",
        "subtopic": "Lok Sabha"
    },
    "Indian Polity > Union Legislature > Members of Parliament": {
        "subject": "Indian Polity",
        "topic": "Union Legislature",
        "subtopic": "Members of Parliament"
    },
    "Indian Polity > Union Legislature > Speaker of the Lok Sabha": {
        "subject": "Indian Polity",
        "topic": "Union Legislature",
        "subtopic": "Speaker of the Lok Sabha"
    },
    "Indian Polity > Union Legislature > Chairman of Rajya Sabha": {
        "subject": "Indian Polity",
        "topic": "Union Legislature",
        "subtopic": "Chairman of Rajya Sabha"
    },
    "Indian Polity > Union Legislature > Parliament - Functioning": {
        "subject": "Indian Polity",
        "topic": "Union Legislature",
        "subtopic": "Parliament - Functioning"
    },
    "Indian Polity > Union Legislature > Bills- enactment/procedure, stages in passing bills etc": {
        "subject": "Indian Polity",
        "topic": "Union Legislature",
        "subtopic": "Bills- enactment/procedure, stages in passing bills etc"
    },
    "Indian Polity > Union Legislature > Budget": {
        "subject": "Indian Polity",
        "topic": "Union Legislature",
        "subtopic": "Budget"
    },
    "Indian Polity > Union Legislature > Powers and functions of parliament Legislative": {
        "subject": "Indian Polity",
        "topic": "Union Legislature",
        "subtopic": "Powers and functions of parliament Legislative"
    },
    "Indian Polity > Union Legislature > Position of Rajya Sabha": {
        "subject": "Indian Polity",
        "topic": "Union Legislature",
        "subtopic": "Position of Rajya Sabha"
    },
    "Indian Polity > Union Legislature > Cabinet committees": {
        "subject": "Indian Polity",
        "topic": "Union Legislature",
        "subtopic": "Cabinet committees"
    },
    "Indian Polity > Union Legislature > Parliamentary committees": {
        "subject": "Indian Polity",
        "topic": "Union Legislature",
        "subtopic": "Parliamentary committees"
    },
    "Indian Polity > Union Legislature > Parliamentary forums": {
        "subject": "Indian Polity",
        "topic": "Union Legislature",
        "subtopic": "Parliamentary forums"
    },
    "Indian Polity > Union Legislature > Parliament privileges": {
        "subject": "Indian Polity",
        "topic": "Union Legislature",
        "subtopic": "Parliament privileges"
    },
    "Indian Polity > State Executive > Governor": {
        "subject": "Indian Polity",
        "topic": "State Executive",
        "subtopic": "Governor"
    },
    "Indian Polity > State Executive > Comparison between Governor and President": {
        "subject": "Indian Polity",
        "topic": "State Executive",
        "subtopic": "Comparison between Governor and President"
    },
    "Indian Polity > State Executive > Chief Minister": {
        "subject": "Indian Polity",
        "topic": "State Executive",
        "subtopic": "Chief Minister"
    },
    "Indian Polity > State Executive > State council of ministers": {
        "subject": "Indian Polity",
        "topic": "State Executive",
        "subtopic": "State council of ministers"
    },
    "Indian Polity > State Legislature > Composition of Two Houses": {
        "subject": "Indian Polity",
        "topic": "State Legislature",
        "subtopic": "Composition of Two Houses"
    },
    "Indian Polity > State Legislature > Duration of Two Houses": {
        "subject": "Indian Polity",
        "topic": "State Legislature",
        "subtopic": "Duration of Two Houses"
    },
    "Indian Polity > State Legislature > Powers and functions": {
        "subject": "Indian Polity",
        "topic": "State Legislature",
        "subtopic": "Powers and functions"
    },
    "Indian Polity > State Legislature > Membership of State Legislature": {
        "subject": "Indian Polity",
        "topic": "State Legislature",
        "subtopic": "Membership of State Legislature"
    },
    "Indian Polity > State Legislature > Presiding Officers of State Legislature": {
        "subject": "Indian Polity",
        "topic": "State Legislature",
        "subtopic": "Presiding Officers of State Legislature"
    },
    "Indian Polity > State Legislature > Governor assent to bill": {
        "subject": "Indian Polity",
        "topic": "State Legislature",
        "subtopic": "Governor assent to bill"
    },
    "Indian Polity > State Legislature > Legislative Procedure in State Legislature": {
        "subject": "Indian Polity",
        "topic": "State Legislature",
        "subtopic": "Legislative Procedure in State Legislature"
    },
    "Indian Polity > State Legislature > Position of Legislative Counci": {
        "subject": "Indian Polity",
        "topic": "State Legislature",
        "subtopic": "Position of Legislative Counci"
    },
    "Indian Polity > State Legislature > State legislature comparison with parliament": {
        "subject": "Indian Polity",
        "topic": "State Legislature",
        "subtopic": "State legislature comparison with parliament"
    },
    "Indian Polity > State Legislature > Position of state legislative council w.r.t legislative assembly and Rajya Sabha": {
        "subject": "Indian Polity",
        "topic": "State Legislature",
        "subtopic": "Position of state legislative council w.r.t legislative assembly and Rajya Sabha"
    },
    "Indian Polity > State Legislature > Sessions of State Legislature": {
        "subject": "Indian Polity",
        "topic": "State Legislature",
        "subtopic": "Sessions of State Legislature"
    },
    "Indian Polity > Judiciary > Supreme Court": {
        "subject": "Indian Polity",
        "topic": "Judiciary",
        "subtopic": "Supreme Court"
    },
    "Indian Polity > Judiciary > High court": {
        "subject": "Indian Polity",
        "topic": "Judiciary",
        "subtopic": "High court"
    },
    "Indian Polity > Judiciary > Jurisdiction and Power": {
        "subject": "Indian Polity",
        "topic": "Judiciary",
        "subtopic": "Jurisdiction and Power"
    },
    "Indian Polity > Judiciary > Judicial review &  judicial activism": {
        "subject": "Indian Polity",
        "topic": "Judiciary",
        "subtopic": "Judicial review &  judicial activism"
    },
    "Indian Polity > Judiciary > Subordinate courts": {
        "subject": "Indian Polity",
        "topic": "Judiciary",
        "subtopic": "Subordinate courts"
    },
    "Indian Polity > Local Self Government > Panchayati Raj": {
        "subject": "Indian Polity",
        "topic": "Local Self Government",
        "subtopic": "Panchayati Raj"
    },
    "Indian Polity > Local Self Government > Municipalities": {
        "subject": "Indian Polity",
        "topic": "Local Self Government",
        "subtopic": "Municipalities"
    },
    "Indian Polity > Local Self Government > committees": {
        "subject": "Indian Polity",
        "topic": "Local Self Government",
        "subtopic": "committees"
    },
    "Indian Polity > Centre - State Relationships > Inter-state relation": {
        "subject": "Indian Polity",
        "topic": "Centre - State Relationships",
        "subtopic": "Inter-state relation"
    },
    "Indian Polity > Centre - State Relationships > Legislative relations": {
        "subject": "Indian Polity",
        "topic": "Centre - State Relationships",
        "subtopic": "Legislative relations"
    },
    "Indian Polity > Centre - State Relationships > Administrative relations": {
        "subject": "Indian Polity",
        "topic": "Centre - State Relationships",
        "subtopic": "Administrative relations"
    },
    "Indian Polity > Centre - State Relationships > Financial relation": {
        "subject": "Indian Polity",
        "topic": "Centre - State Relationships",
        "subtopic": "Financial relation"
    },
    "Indian Polity > Centre - State Relationships > Effects of emergencies": {
        "subject": "Indian Polity",
        "topic": "Centre - State Relationships",
        "subtopic": "Effects of emergencies"
    },
    "Indian Polity > Centre - State Relationships > Committees/Commission related to Centre state relations": {
        "subject": "Indian Polity",
        "topic": "Centre - State Relationships",
        "subtopic": "Committees/Commission related to Centre state relations"
    },
    "Indian Polity > Emergency Provisions > National Emergency": {
        "subject": "Indian Polity",
        "topic": "Emergency Provisions",
        "subtopic": "National Emergency"
    },
    "Indian Polity > Emergency Provisions > President’s Rule": {
        "subject": "Indian Polity",
        "topic": "Emergency Provisions",
        "subtopic": "President’s Rule"
    },
    "Indian Polity > Emergency Provisions > Financial Emergency": {
        "subject": "Indian Polity",
        "topic": "Emergency Provisions",
        "subtopic": "Financial Emergency"
    },
    "Indian Polity > Emergency Provisions > Impact of emergency": {
        "subject": "Indian Polity",
        "topic": "Emergency Provisions",
        "subtopic": "Impact of emergency"
    },
    "Indian Polity > Constitutional Bodies > Election Commission": {
        "subject": "Indian Polity",
        "topic": "Constitutional Bodies",
        "subtopic": "Election Commission"
    },
    "Indian Polity > Constitutional Bodies > UPSC, SPSC and JPSC": {
        "subject": "Indian Polity",
        "topic": "Constitutional Bodies",
        "subtopic": "UPSC, SPSC and JPSC"
    },
    "Indian Polity > Constitutional Bodies > National Commissions  SC/ ST/ Backward classes": {
        "subject": "Indian Polity",
        "topic": "Constitutional Bodies",
        "subtopic": "National Commissions  SC/ ST/ Backward classes"
    },
    "Indian Polity > Constitutional Bodies > Comptroller and Auditor General of India": {
        "subject": "Indian Polity",
        "topic": "Constitutional Bodies",
        "subtopic": "Comptroller and Auditor General of India"
    },
    "Indian Polity > Constitutional Bodies > Attorney General": {
        "subject": "Indian Polity",
        "topic": "Constitutional Bodies",
        "subtopic": "Attorney General"
    },
    "Indian Polity > Constitutional Bodies > Advocate general": {
        "subject": "Indian Polity",
        "topic": "Constitutional Bodies",
        "subtopic": "Advocate general"
    },
    "Indian Polity > Constitutional Bodies > Solicitor general": {
        "subject": "Indian Polity",
        "topic": "Constitutional Bodies",
        "subtopic": "Solicitor general"
    },
    "Indian Polity > Non-Constitutional Bodies > National human rights commission & State human rights commission": {
        "subject": "Indian Polity",
        "topic": "Non-Constitutional Bodies",
        "subtopic": "National human rights commission & State human rights commission"
    },
    "Indian Polity > Non-Constitutional Bodies > Central information commission & State information commission": {
        "subject": "Indian Polity",
        "topic": "Non-Constitutional Bodies",
        "subtopic": "Central information commission & State information commission"
    },
    "Indian Polity > Non-Constitutional Bodies > Central vigilance commission": {
        "subject": "Indian Polity",
        "topic": "Non-Constitutional Bodies",
        "subtopic": "Central vigilance commission"
    },
    "Indian Polity > Non-Constitutional Bodies > Lokpal and Lokayukta": {
        "subject": "Indian Polity",
        "topic": "Non-Constitutional Bodies",
        "subtopic": "Lokpal and Lokayukta"
    },
    "Indian Polity > Non-Constitutional Bodies > National law commission": {
        "subject": "Indian Polity",
        "topic": "Non-Constitutional Bodies",
        "subtopic": "National law commission"
    },
    "Indian Polity > Non-Constitutional Bodies > National green tribunal": {
        "subject": "Indian Polity",
        "topic": "Non-Constitutional Bodies",
        "subtopic": "National green tribunal"
    },
    "Indian Polity > Non-Constitutional Bodies > Food safety and standard authority of India": {
        "subject": "Indian Polity",
        "topic": "Non-Constitutional Bodies",
        "subtopic": "Food safety and standard authority of India"
    },
    "Indian Polity > Non-Constitutional Bodies > Bureau of Indian standards": {
        "subject": "Indian Polity",
        "topic": "Non-Constitutional Bodies",
        "subtopic": "Bureau of Indian standards"
    },
    "Indian Polity > Non-Constitutional Bodies > Competition commission of India": {
        "subject": "Indian Polity",
        "topic": "Non-Constitutional Bodies",
        "subtopic": "Competition commission of India"
    },
    "Indian Polity > Non-Constitutional Bodies > Non - Statutory Bodies": {
        "subject": "Indian Polity",
        "topic": "Non-Constitutional Bodies",
        "subtopic": "Non - Statutory Bodies"
    },
    "Indian Polity > Empowerment of Women > Women Empowerment Schemes in India": {
        "subject": "Indian Polity",
        "topic": "Empowerment of Women",
        "subtopic": "Women Empowerment Schemes in India"
    },
    "Indian Polity > Empowerment of Women > Constitutional Provisions": {
        "subject": "Indian Polity",
        "topic": "Empowerment of Women",
        "subtopic": "Constitutional Provisions"
    },
    "Indian Polity > Empowerment of Women > Important Acts": {
        "subject": "Indian Polity",
        "topic": "Empowerment of Women",
        "subtopic": "Important Acts"
    },
    "Indian Polity > Consumer Protection Forums > Consumer Protection Act 2019": {
        "subject": "Indian Polity",
        "topic": "Consumer Protection Forums",
        "subtopic": "Consumer Protection Act 2019"
    },
    "Indian Polity > Political parties and political system in India > Recognised parties": {
        "subject": "Indian Polity",
        "topic": "Political parties and political system in India",
        "subtopic": "Recognised parties"
    },
    "Indian Polity > Political parties and political system in India > non - recognised parties": {
        "subject": "Indian Polity",
        "topic": "Political parties and political system in India",
        "subtopic": "non - recognised parties"
    },
    "Indian Polity > Election > Representation of people act 1950 & 1951": {
        "subject": "Indian Polity",
        "topic": "Election",
        "subtopic": "Representation of people act 1950 & 1951"
    },
    "Indian Economy & Development Administration in Tamilnadu > Basics of Economy > Microeconomics vs Macroeconomics": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Basics of Economy",
        "subtopic": "Microeconomics vs Macroeconomics"
    },
    "Indian Economy & Development Administration in Tamilnadu > Basics of Economy > Sectors of Economy-Primary, Secondary and Tertiary Sector": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Basics of Economy",
        "subtopic": "Sectors of Economy-Primary, Secondary and Tertiary Sector"
    },
    "Indian Economy & Development Administration in Tamilnadu > Basics of Economy > Factors of Production": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Basics of Economy",
        "subtopic": "Factors of Production"
    },
    "Indian Economy & Development Administration in Tamilnadu > Basics of Economy > Type of Economic System": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Basics of Economy",
        "subtopic": "Type of Economic System"
    },
    "Indian Economy & Development Administration in Tamilnadu > Basics of Economy > Growth and Development": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Basics of Economy",
        "subtopic": "Growth and Development"
    },
    "Indian Economy & Development Administration in Tamilnadu > Nature of Indian Economy > Strengths of Indian Economy": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Nature of Indian Economy",
        "subtopic": "Strengths of Indian Economy"
    },
    "Indian Economy & Development Administration in Tamilnadu > Nature of Indian Economy > Weakness of Indian Economy": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Nature of Indian Economy",
        "subtopic": "Weakness of Indian Economy"
    },
    "Indian Economy & Development Administration in Tamilnadu > Nature of Indian Economy > Natural Resources": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Nature of Indian Economy",
        "subtopic": "Natural Resources"
    },
    "Indian Economy & Development Administration in Tamilnadu > Five-year plan > Economic Planning in India": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Five-year plan",
        "subtopic": "Economic Planning in India"
    },
    "Indian Economy & Development Administration in Tamilnadu > Five-year plan > Planning Commission of India": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Five-year plan",
        "subtopic": "Planning Commission of India"
    },
    "Indian Economy & Development Administration in Tamilnadu > Five-year plan > National Development Council (NDC)s": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Five-year plan",
        "subtopic": "National Development Council (NDC)s"
    },
    "Indian Economy & Development Administration in Tamilnadu > Five-year plan > Five Year Plan": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Five-year plan",
        "subtopic": "Five Year Plan"
    },
    "Indian Economy & Development Administration in Tamilnadu > Five-year plan > Niti Aayog": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Five-year plan",
        "subtopic": "Niti Aayog"
    },
    "Indian Economy & Development Administration in Tamilnadu > National Income > Basic concepts of national income": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "National Income",
        "subtopic": "Basic concepts of national income"
    },
    "Indian Economy & Development Administration in Tamilnadu > National Income > Money": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "National Income",
        "subtopic": "Money"
    },
    "Indian Economy & Development Administration in Tamilnadu > National Income > Money, Demand and Supply": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "National Income",
        "subtopic": "Money, Demand and Supply"
    },
    "Indian Economy & Development Administration in Tamilnadu > Monetary Policy > Expansionary Vs. Contractionary": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Monetary Policy",
        "subtopic": "Expansionary Vs. Contractionary"
    },
    "Indian Economy & Development Administration in Tamilnadu > Monetary Policy > Objectives of Monetary Policy": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Monetary Policy",
        "subtopic": "Objectives of Monetary Policy"
    },
    "Indian Economy & Development Administration in Tamilnadu > Monetary Policy > Composition of the MPC": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Monetary Policy",
        "subtopic": "Composition of the MPC"
    },
    "Indian Economy & Development Administration in Tamilnadu > Monetary Policy > Methods of Credit Control": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Monetary Policy",
        "subtopic": "Methods of Credit Control"
    },
    "Indian Economy & Development Administration in Tamilnadu > Monetary Policy > Inflation": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Monetary Policy",
        "subtopic": "Inflation"
    },
    "Indian Economy & Development Administration in Tamilnadu > Monetary Policy > Meaning of Deflation, Disinflation and Stagflation": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Monetary Policy",
        "subtopic": "Meaning of Deflation, Disinflation and Stagflation"
    },
    "Indian Economy & Development Administration in Tamilnadu > Monetary Policy > Measurement of Inflation": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Monetary Policy",
        "subtopic": "Measurement of Inflation"
    },
    "Indian Economy & Development Administration in Tamilnadu > Banking > Reserve Bank of India": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Banking",
        "subtopic": "Reserve Bank of India"
    },
    "Indian Economy & Development Administration in Tamilnadu > Banking > Scheduled and Non Scheduled Banks": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Banking",
        "subtopic": "Scheduled and Non Scheduled Banks"
    },
    "Indian Economy & Development Administration in Tamilnadu > Banking > Non-Banking Financial Companies(NBFC)": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Banking",
        "subtopic": "Non-Banking Financial Companies(NBFC)"
    },
    "Indian Economy & Development Administration in Tamilnadu > Banking > All India Financial Institutions (AIFI)- Non Banks": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Banking",
        "subtopic": "All India Financial Institutions (AIFI)- Non Banks"
    },
    "Indian Economy & Development Administration in Tamilnadu > Banking > Issue of Banking Sector": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Banking",
        "subtopic": "Issue of Banking Sector"
    },
    "Indian Economy & Development Administration in Tamilnadu > Fiscal Policy > Meaning of Public Finance": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Fiscal Policy",
        "subtopic": "Meaning of Public Finance"
    },
    "Indian Economy & Development Administration in Tamilnadu > Fiscal Policy > Budgetary Deficits": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Fiscal Policy",
        "subtopic": "Budgetary Deficits"
    },
    "Indian Economy & Development Administration in Tamilnadu > Fiscal Policy > Bodies related to Budgeting": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Fiscal Policy",
        "subtopic": "Bodies related to Budgeting"
    },
    "Indian Economy & Development Administration in Tamilnadu > Fiscal Policy > Basics of Budget": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Fiscal Policy",
        "subtopic": "Basics of Budget"
    },
    "Indian Economy & Development Administration in Tamilnadu > Fiscal Policy > Components of Budget": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Fiscal Policy",
        "subtopic": "Components of Budget"
    },
    "Indian Economy & Development Administration in Tamilnadu > Fiscal Policy > Types of Budget": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Fiscal Policy",
        "subtopic": "Types of Budget"
    },
    "Indian Economy & Development Administration in Tamilnadu > Taxation > Direct Taxes": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Taxation",
        "subtopic": "Direct Taxes"
    },
    "Indian Economy & Development Administration in Tamilnadu > Taxation > Indirect Taxes": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Taxation",
        "subtopic": "Indirect Taxes"
    },
    "Indian Economy & Development Administration in Tamilnadu > Taxation > GST": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Taxation",
        "subtopic": "GST"
    },
    "Indian Economy & Development Administration in Tamilnadu > Taxation > Miscellaneous": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Taxation",
        "subtopic": "Miscellaneous"
    },
    "Indian Economy & Development Administration in Tamilnadu > Resource sharing between Union & State Governments > The sources of income as prescribed by the Constitution of India for the Central Government": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Resource sharing between Union & State Governments",
        "subtopic": "The sources of income as prescribed by the Constitution of India for the Central Government"
    },
    "Indian Economy & Development Administration in Tamilnadu > Resource sharing between Union & State Governments > Earnings of state government": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Resource sharing between Union & State Governments",
        "subtopic": "Earnings of state government"
    },
    "Indian Economy & Development Administration in Tamilnadu > Resource sharing between Union & State Governments > Taxes Levied & Collected by The Union but Assigned to The States": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Resource sharing between Union & State Governments",
        "subtopic": "Taxes Levied & Collected by The Union but Assigned to The States"
    },
    "Indian Economy & Development Administration in Tamilnadu > Resource sharing between Union & State Governments > Duties Levied By The Union but Collected & Appropriated by The States": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Resource sharing between Union & State Governments",
        "subtopic": "Duties Levied By The Union but Collected & Appropriated by The States"
    },
    "Indian Economy & Development Administration in Tamilnadu > Resource sharing between Union & State Governments > Taxes which are Levied and Collected by the Union but which may be Distributed between the Union and the States": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Resource sharing between Union & State Governments",
        "subtopic": "Taxes which are Levied and Collected by the Union but which may be Distributed between the Union and the States"
    },
    "Indian Economy & Development Administration in Tamilnadu > Resource sharing between Union & State Governments > Finance Commission": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Resource sharing between Union & State Governments",
        "subtopic": "Finance Commission"
    },
    "Indian Economy & Development Administration in Tamilnadu > Structure of Indian Economy & Employment Generation > Main Sectors in India’s Economy": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Structure of Indian Economy & Employment Generation",
        "subtopic": "Main Sectors in India’s Economy"
    },
    "Indian Economy & Development Administration in Tamilnadu > Structure of Indian Economy & Employment Generation > Other Sectors in India’s Economy": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Structure of Indian Economy & Employment Generation",
        "subtopic": "Other Sectors in India’s Economy"
    },
    "Indian Economy & Development Administration in Tamilnadu > Structure of Indian Economy & Employment Generation > Initiatives for Employment Generation": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Structure of Indian Economy & Employment Generation",
        "subtopic": "Initiatives for Employment Generation"
    },
    "Indian Economy & Development Administration in Tamilnadu > Land Reforms & Agriculture > Role of Agriculture in Indian Economy": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Land Reforms & Agriculture",
        "subtopic": "Role of Agriculture in Indian Economy"
    },
    "Indian Economy & Development Administration in Tamilnadu > Land Reforms & Agriculture > Application of Science and Technology in Agriculture": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Land Reforms & Agriculture",
        "subtopic": "Application of Science and Technology in Agriculture"
    },
    "Indian Economy & Development Administration in Tamilnadu > Land Reforms & Agriculture > Land Reforms": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Land Reforms & Agriculture",
        "subtopic": "Land Reforms"
    },
    "Indian Economy & Development Administration in Tamilnadu > Land Reforms & Agriculture > Cropping Pattern in India": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Land Reforms & Agriculture",
        "subtopic": "Cropping Pattern in India"
    },
    "Indian Economy & Development Administration in Tamilnadu > Land Reforms & Agriculture > Types of crops in India": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Land Reforms & Agriculture",
        "subtopic": "Types of crops in India"
    },
    "Indian Economy & Development Administration in Tamilnadu > Land Reforms & Agriculture > Major Producer of the Crops in India": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Land Reforms & Agriculture",
        "subtopic": "Major Producer of the Crops in India"
    },
    "Indian Economy & Development Administration in Tamilnadu > Land Reforms & Agriculture > Cropping Seasons in India": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Land Reforms & Agriculture",
        "subtopic": "Cropping Seasons in India"
    },
    "Indian Economy & Development Administration in Tamilnadu > Land Reforms & Agriculture > Green Revolution": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Land Reforms & Agriculture",
        "subtopic": "Green Revolution"
    },
    "Indian Economy & Development Administration in Tamilnadu > Land Reforms & Agriculture > Agriculture Related Schemes": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Land Reforms & Agriculture",
        "subtopic": "Agriculture Related Schemes"
    },
    "Indian Economy & Development Administration in Tamilnadu > Land Reforms & Agriculture > Irrigation": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Land Reforms & Agriculture",
        "subtopic": "Irrigation"
    },
    "Indian Economy & Development Administration in Tamilnadu > Land Reforms & Agriculture > PDS": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Land Reforms & Agriculture",
        "subtopic": "PDS"
    },
    "Indian Economy & Development Administration in Tamilnadu > Land Reforms & Agriculture > Minimum support prices (MSP), Procurement prices, Issue Price, Retail prices": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Land Reforms & Agriculture",
        "subtopic": "Minimum support prices (MSP), Procurement prices, Issue Price, Retail prices"
    },
    "Indian Economy & Development Administration in Tamilnadu > Land Reforms & Agriculture > Rural Welfare Oriented Programmes": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Land Reforms & Agriculture",
        "subtopic": "Rural Welfare Oriented Programmes"
    },
    "Indian Economy & Development Administration in Tamilnadu > Industrial growth > Types of Industries": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Industrial growth",
        "subtopic": "Types of Industries"
    },
    "Indian Economy & Development Administration in Tamilnadu > Industrial growth > Core Industries in India": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Industrial growth",
        "subtopic": "Core Industries in India"
    },
    "Indian Economy & Development Administration in Tamilnadu > Industrial growth > State-wise Distribution of Industries": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Industrial growth",
        "subtopic": "State-wise Distribution of Industries"
    },
    "Indian Economy & Development Administration in Tamilnadu > Industrial growth > Industrial Policies": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Industrial growth",
        "subtopic": "Industrial Policies"
    },
    "Indian Economy & Development Administration in Tamilnadu > Industrial growth > Public Sector Enterprises": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Industrial growth",
        "subtopic": "Public Sector Enterprises"
    },
    "Indian Economy & Development Administration in Tamilnadu > Rural Welfare Oriented Programmes > Rural Welfare Oriented Programmes": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Rural Welfare Oriented Programmes",
        "subtopic": "Rural Welfare Oriented Programmes"
    },
    "Indian Economy & Development Administration in Tamilnadu > Social Problems > Population": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Social Problems",
        "subtopic": "Population"
    },
    "Indian Economy & Development Administration in Tamilnadu > Social Problems > Education": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Social Problems",
        "subtopic": "Education"
    },
    "Indian Economy & Development Administration in Tamilnadu > Social Problems > Health": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Social Problems",
        "subtopic": "Health"
    },
    "Indian Economy & Development Administration in Tamilnadu > Social Problems > Employment": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Social Problems",
        "subtopic": "Employment"
    },
    "Indian Economy & Development Administration in Tamilnadu > Social Problems > Poverty": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Social Problems",
        "subtopic": "Poverty"
    },
    "Indian Economy & Development Administration in Tamilnadu > Human Development Index > Three indicators": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Human Development Index",
        "subtopic": "Three indicators"
    },
    "Indian Economy & Development Administration in Tamilnadu > Human Development Index > Human Development Report": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Human Development Index",
        "subtopic": "Human Development Report"
    },
    "Indian Economy & Development Administration in Tamilnadu > Human Development Index > 5 Indices of Human Development Report": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Human Development Index",
        "subtopic": "5 Indices of Human Development Report"
    },
    "Indian Economy & Development Administration in Tamilnadu > Human Development Index > Important Human Development Indicators of Tamil Nadu": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Human Development Index",
        "subtopic": "Important Human Development Indicators of Tamil Nadu"
    },
    "Indian Economy & Development Administration in Tamilnadu > Social Reform Movements in Tamil Nadu > Social Reformers of Tamilnadu": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Social Reform Movements in Tamil Nadu",
        "subtopic": "Social Reformers of Tamilnadu"
    },
    "Indian Economy & Development Administration in Tamilnadu > Political parties & Welfare schemes > Political Parties": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Political parties & Welfare schemes",
        "subtopic": "Political Parties"
    },
    "Indian Economy & Development Administration in Tamilnadu > Political parties & Welfare schemes > Recognized Tamil Nadu State Parties": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Political parties & Welfare schemes",
        "subtopic": "Recognized Tamil Nadu State Parties"
    },
    "Indian Economy & Development Administration in Tamilnadu > Political parties & Welfare schemes > Achievements of the Parties": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Political parties & Welfare schemes",
        "subtopic": "Achievements of the Parties"
    },
    "Indian Economy & Development Administration in Tamilnadu > Political parties & Welfare schemes > Social Welfare Schemes by Tamil Nadu": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Political parties & Welfare schemes",
        "subtopic": "Social Welfare Schemes by Tamil Nadu"
    },
    "Indian Economy & Development Administration in Tamilnadu > Reservation Policy > Reservation Policy in Tamilnadu": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Reservation Policy",
        "subtopic": "Reservation Policy in Tamilnadu"
    },
    "Indian Economy & Development Administration in Tamilnadu > Reservation Policy > Reservation Policy in India": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Reservation Policy",
        "subtopic": "Reservation Policy in India"
    },
    "Indian Economy & Development Administration in Tamilnadu > Social Justice & Social Harmony > Social Justice Theories": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Social Justice & Social Harmony",
        "subtopic": "Social Justice Theories"
    },
    "Indian Economy & Development Administration in Tamilnadu > Social Justice & Social Harmony > Constitutional Provisions of social Justice": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Social Justice & Social Harmony",
        "subtopic": "Constitutional Provisions of social Justice"
    },
    "Indian Economy & Development Administration in Tamilnadu > Social Justice & Social Harmony > Justice Party Contribution": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Social Justice & Social Harmony",
        "subtopic": "Justice Party Contribution"
    },
    "Indian Economy & Development Administration in Tamilnadu > Social Justice & Social Harmony > Welfare and empowerment of SCs, STs, differently abled, women, transgender, aged and senior citizens, child rights": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Social Justice & Social Harmony",
        "subtopic": "Welfare and empowerment of SCs, STs, differently abled, women, transgender, aged and senior citizens, child rights"
    },
    "Indian Economy & Development Administration in Tamilnadu > Social Justice & Social Harmony > Various Commissions": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Social Justice & Social Harmony",
        "subtopic": "Various Commissions"
    },
    "Indian Economy & Development Administration in Tamilnadu > Economic Trends in Tamil Nadu > Highlights of Tamil Nadu Economy": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Economic Trends in Tamil Nadu",
        "subtopic": "Highlights of Tamil Nadu Economy"
    },
    "Indian Economy & Development Administration in Tamilnadu > Economic Trends in Tamil Nadu > GI Tags": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Economic Trends in Tamil Nadu",
        "subtopic": "GI Tags"
    },
    "Indian Economy & Development Administration in Tamilnadu > Economic Trends in Tamil Nadu > Economic Policies": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Economic Trends in Tamil Nadu",
        "subtopic": "Economic Policies"
    },
    "Indian Economy & Development Administration in Tamilnadu > Economic Trends in Tamil Nadu > Budget Highlights": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Economic Trends in Tamil Nadu",
        "subtopic": "Budget Highlights"
    },
    "Indian Economy & Development Administration in Tamilnadu > Education and Health Systems in Tamil Nadu > Tamil Nadu Educational System": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Education and Health Systems in Tamil Nadu",
        "subtopic": "Tamil Nadu Educational System"
    },
    "Indian Economy & Development Administration in Tamilnadu > Education and Health Systems in Tamil Nadu > Literacy in Tamil Nadu": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Education and Health Systems in Tamil Nadu",
        "subtopic": "Literacy in Tamil Nadu"
    },
    "Indian Economy & Development Administration in Tamilnadu > Education and Health Systems in Tamil Nadu > Education & Health Related Constitutional Provisions, Acts, Government Schemes": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Education and Health Systems in Tamil Nadu",
        "subtopic": "Education & Health Related Constitutional Provisions, Acts, Government Schemes"
    },
    "Indian Economy & Development Administration in Tamilnadu > Education and Health Systems in Tamil Nadu > Education Policy - Tamil Nadu and India": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Education and Health Systems in Tamil Nadu",
        "subtopic": "Education Policy - Tamil Nadu and India"
    },
    "Indian Economy & Development Administration in Tamilnadu > Education and Health Systems in Tamil Nadu > Health Policy - Tamil Nadu and India": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Education and Health Systems in Tamil Nadu",
        "subtopic": "Health Policy - Tamil Nadu and India"
    },
    "Indian Economy & Development Administration in Tamilnadu > Education and Health Systems in Tamil Nadu > Health Systems in Tamil Nadu": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Education and Health Systems in Tamil Nadu",
        "subtopic": "Health Systems in Tamil Nadu"
    },
    "Indian Economy & Development Administration in Tamilnadu > Education and Health Systems in Tamil Nadu > Health Indicators": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Education and Health Systems in Tamil Nadu",
        "subtopic": "Health Indicators"
    },
    "Indian Economy & Development Administration in Tamilnadu > Education and Health Systems in Tamil Nadu > Health Care Institutions in TN - Primary, Secondary and Tertiary": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Education and Health Systems in Tamil Nadu",
        "subtopic": "Health Care Institutions in TN - Primary, Secondary and Tertiary"
    },
    "Indian Economy & Development Administration in Tamilnadu > Geography of Tamil Nadu > Physiographic Divisions": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Geography of Tamil Nadu",
        "subtopic": "Physiographic Divisions"
    },
    "Indian Economy & Development Administration in Tamilnadu > Geography of Tamil Nadu > Land Area Extent": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Geography of Tamil Nadu",
        "subtopic": "Land Area Extent"
    },
    "Indian Economy & Development Administration in Tamilnadu > Geography of Tamil Nadu > Climate": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Geography of Tamil Nadu",
        "subtopic": "Climate"
    },
    "Indian Economy & Development Administration in Tamilnadu > Geography of Tamil Nadu > Soils": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Geography of Tamil Nadu",
        "subtopic": "Soils"
    },
    "Indian Economy & Development Administration in Tamilnadu > Geography of Tamil Nadu > Natural Vegetation": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Geography of Tamil Nadu",
        "subtopic": "Natural Vegetation"
    },
    "Indian Economy & Development Administration in Tamilnadu > Geography of Tamil Nadu > Agriculture": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Geography of Tamil Nadu",
        "subtopic": "Agriculture"
    },
    "Indian Economy & Development Administration in Tamilnadu > Geography of Tamil Nadu > Livestock": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Geography of Tamil Nadu",
        "subtopic": "Livestock"
    },
    "Indian Economy & Development Administration in Tamilnadu > Geography of Tamil Nadu > water sources": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Geography of Tamil Nadu",
        "subtopic": "water sources"
    },
    "Indian Economy & Development Administration in Tamilnadu > Geography of Tamil Nadu > Mineral resources": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Geography of Tamil Nadu",
        "subtopic": "Mineral resources"
    },
    "Indian Economy & Development Administration in Tamilnadu > Geography of Tamil Nadu > Industries": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Geography of Tamil Nadu",
        "subtopic": "Industries"
    },
    "Indian Economy & Development Administration in Tamilnadu > Geography of Tamil Nadu > Transport and communication": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Geography of Tamil Nadu",
        "subtopic": "Transport and communication"
    },
    "Indian Economy & Development Administration in Tamilnadu > Geography of Tamil Nadu > Demography": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Geography of Tamil Nadu",
        "subtopic": "Demography"
    },
    "Indian Economy & Development Administration in Tamilnadu > Tamil Nadu e-Governance > Institutional frameworks for e-governance": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Tamil Nadu e-Governance",
        "subtopic": "Institutional frameworks for e-governance"
    },
    "Indian Economy & Development Administration in Tamilnadu > Tamil Nadu e-Governance > Core Infrastructure of Information Technology": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Tamil Nadu e-Governance",
        "subtopic": "Core Infrastructure of Information Technology"
    },
    "Indian Economy & Development Administration in Tamilnadu > Tamil Nadu e-Governance > e-Governance programs": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Tamil Nadu e-Governance",
        "subtopic": "e-Governance programs"
    },
    "Indian Economy & Development Administration in Tamilnadu > Tamil Nadu e-Governance > e-governance policy": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Tamil Nadu e-Governance",
        "subtopic": "e-governance policy"
    },
    "Indian Economy & Development Administration in Tamilnadu > Achievements of Tamil Nadu in Various Fields > Achievements and Awards": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Achievements of Tamil Nadu in Various Fields",
        "subtopic": "Achievements and Awards"
    },
    "Indian Economy & Development Administration in Tamilnadu > Achievements of Tamil Nadu in Various Fields > E-Governance Initiatives in Tamilnadu": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Achievements of Tamil Nadu in Various Fields",
        "subtopic": "E-Governance Initiatives in Tamilnadu"
    },
    "Indian Economy & Development Administration in Tamilnadu > Achievements of Tamil Nadu in Various Fields > Performance of Tamil Nadu Economy": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Achievements of Tamil Nadu in Various Fields",
        "subtopic": "Performance of Tamil Nadu Economy"
    },
    "Indian Economy & Development Administration in Tamilnadu > Achievements of Tamil Nadu in Various Fields > Tamil Nadu related recent Survey, data, Indices, Ranking, Reports, etc": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Achievements of Tamil Nadu in Various Fields",
        "subtopic": "Tamil Nadu related recent Survey, data, Indices, Ranking, Reports, etc"
    },
    "Indian Economy & Development Administration in Tamilnadu > Public awareness and General administration > Public awareness and General administration": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Public awareness and General administration",
        "subtopic": "Public awareness and General administration"
    },
    "Indian Economy & Development Administration in Tamilnadu > Current socio-economic issues > Current socio-economic issues": {
        "subject": "Indian Economy & Development Administration in Tamilnadu",
        "topic": "Current socio-economic issues",
        "subtopic": "Current socio-economic issues"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > History of Tamil Society > Origin of the Tamils": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "History of Tamil Society",
        "subtopic": "Origin of the Tamils"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > History of Tamil Society > Sangam Age Three Dynasties (Chera, Chola, Pandya)": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "History of Tamil Society",
        "subtopic": "Sangam Age Three Dynasties (Chera, Chola, Pandya)"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > History of Tamil Society > Sangam Age Tamil Cities": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "History of Tamil Society",
        "subtopic": "Sangam Age Tamil Cities"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > archaeological discoveries > Excavated Sites by Tamil Nadu Archaeology Department": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "archaeological discoveries",
        "subtopic": "Excavated Sites by Tamil Nadu Archaeology Department"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > archaeological discoveries > Non-Tamil Language References": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "archaeological discoveries",
        "subtopic": "Non-Tamil Language References"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > archaeological discoveries > Accounts of Foreigners": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "archaeological discoveries",
        "subtopic": "Accounts of Foreigners"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Tamil literature > Eight Anthologies (Ettuthokai)": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Tamil literature",
        "subtopic": "Eight Anthologies (Ettuthokai)"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Tamil literature > Ten Idylls (Pathuppattu)": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Tamil literature",
        "subtopic": "Ten Idylls (Pathuppattu)"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Tamil literature > Eighteen Minor Works (Pathinen Keezhkanakku Noolgal)": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Tamil literature",
        "subtopic": "Eighteen Minor Works (Pathinen Keezhkanakku Noolgal)"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Tamil literature > Five Great Epics (Aimperum Kappiyangal)": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Tamil literature",
        "subtopic": "Five Great Epics (Aimperum Kappiyangal)"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Tamil literature > Five Small Epics (Ainchiru Kappiyangal)": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Tamil literature",
        "subtopic": "Five Small Epics (Ainchiru Kappiyangal)"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Tamil literature > Continuity Poems (Thodarnilai Seiyyulgal)": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Tamil literature",
        "subtopic": "Continuity Poems (Thodarnilai Seiyyulgal)"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Tamil literature > Bhakti Literature": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Tamil literature",
        "subtopic": "Bhakti Literature"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Thirukkural > Secular / Non-Religious Literature": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Thirukkural",
        "subtopic": "Secular / Non-Religious Literature"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Thirukkural > Impact of Thirukkural on Humanity": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Thirukkural",
        "subtopic": "Impact of Thirukkural on Humanity"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Thirukkural > Relation to Everyday Life": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Thirukkural",
        "subtopic": "Relation to Everyday Life"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Thirukkural > Thirukkural and Timeless Values - Humanism, Equality": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Thirukkural",
        "subtopic": "Thirukkural and Timeless Values - Humanism, Equality"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Thirukkural > Philosophical Doctrines in Thirukkural": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Thirukkural",
        "subtopic": "Philosophical Doctrines in Thirukkural"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Thirukkural > Thirukkural in Social, Political, and Economic Events": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Thirukkural",
        "subtopic": "Thirukkural in Social, Political, and Economic Events"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Early agitations aginst British Rule > Nayak Rule in Tamil Nadu": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Early agitations aginst British Rule",
        "subtopic": "Nayak Rule in Tamil Nadu"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Early agitations aginst British Rule > Puli Thevar": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Early agitations aginst British Rule",
        "subtopic": "Puli Thevar"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Early agitations aginst British Rule > Veerapandiya Kattabomman": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Early agitations aginst British Rule",
        "subtopic": "Veerapandiya Kattabomman"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Early agitations aginst British Rule > Maruthu Brothers": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Early agitations aginst British Rule",
        "subtopic": "Maruthu Brothers"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Early agitations aginst British Rule > South Indian Confederacy for Liberation": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Early agitations aginst British Rule",
        "subtopic": "South Indian Confederacy for Liberation"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Early agitations aginst British Rule > Vellore Revolt": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Early agitations aginst British Rule",
        "subtopic": "Vellore Revolt"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Role of Tamil Nadu in freedom struggle > Madras Native Association": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Role of Tamil Nadu in freedom struggle",
        "subtopic": "Madras Native Association"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Role of Tamil Nadu in freedom struggle > Madras Mahajana Sabha": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Role of Tamil Nadu in freedom struggle",
        "subtopic": "Madras Mahajana Sabha"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Role of Tamil Nadu in freedom struggle > Swadeshi Steam Navigation Company": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Role of Tamil Nadu in freedom struggle",
        "subtopic": "Swadeshi Steam Navigation Company"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Role of Tamil Nadu in freedom struggle > Madras Jana Sangam": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Role of Tamil Nadu in freedom struggle",
        "subtopic": "Madras Jana Sangam"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Role of Tamil Nadu in freedom struggle > Home Rule Movement": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Role of Tamil Nadu in freedom struggle",
        "subtopic": "Home Rule Movement"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Role of Tamil Nadu in freedom struggle > Rowlatt Satyagraha": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Role of Tamil Nadu in freedom struggle",
        "subtopic": "Rowlatt Satyagraha"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Role of Tamil Nadu in freedom struggle > Khilafat Movement": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Role of Tamil Nadu in freedom struggle",
        "subtopic": "Khilafat Movement"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Role of Tamil Nadu in freedom struggle > Non-Cooperation Movement": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Role of Tamil Nadu in freedom struggle",
        "subtopic": "Non-Cooperation Movement"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Role of Tamil Nadu in freedom struggle > Neel Statue Satyagraha": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Role of Tamil Nadu in freedom struggle",
        "subtopic": "Neel Statue Satyagraha"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Role of Tamil Nadu in freedom struggle > Simon Commission Boycott": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Role of Tamil Nadu in freedom struggle",
        "subtopic": "Simon Commission Boycott"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Role of Tamil Nadu in freedom struggle > Civil Disobedience Movement": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Role of Tamil Nadu in freedom struggle",
        "subtopic": "Civil Disobedience Movement"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Role of Tamil Nadu in freedom struggle > Individual Satyagraha": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Role of Tamil Nadu in freedom struggle",
        "subtopic": "Individual Satyagraha"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Role of Tamil Nadu in freedom struggle > Quit India Movement": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Role of Tamil Nadu in freedom struggle",
        "subtopic": "Quit India Movement"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Role of women in freedom struggle > Dilliayadi Valliammal": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Role of women in freedom struggle",
        "subtopic": "Dilliayadi Valliammal"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Role of women in freedom struggle > Anjalai Ammal": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Role of women in freedom struggle",
        "subtopic": "Anjalai Ammal"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Role of women in freedom struggle > Ambujathammal": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Role of women in freedom struggle",
        "subtopic": "Ambujathammal"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Role of women in freedom struggle > Dr.Muthulakshmi Reddy": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Role of women in freedom struggle",
        "subtopic": "Dr.Muthulakshmi Reddy"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Role of women in freedom struggle > S. Dharmambal": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Role of women in freedom struggle",
        "subtopic": "S. Dharmambal"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Role of women in freedom struggle > Moovalur Ramamirtham Ammaiyar": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Role of women in freedom struggle",
        "subtopic": "Moovalur Ramamirtham Ammaiyar"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Role of women in freedom struggle > Rukmani Lakshmipathi": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Role of women in freedom struggle",
        "subtopic": "Rukmani Lakshmipathi"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Role of women in freedom struggle > S. R. Kannamma": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Role of women in freedom struggle",
        "subtopic": "S. R. Kannamma"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Role of women in freedom struggle > Nagammaiyar": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Role of women in freedom struggle",
        "subtopic": "Nagammaiyar"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Role of women in freedom struggle > Durgabai Deshmukh": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Role of women in freedom struggle",
        "subtopic": "Durgabai Deshmukh"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Evolution of 19th and 20th century socio-political movements in Tamil Nadu > Ramalinga Adigal (Vallalar)": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Evolution of 19th and 20th century socio-political movements in Tamil Nadu",
        "subtopic": "Ramalinga Adigal (Vallalar)"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Evolution of 19th and 20th century socio-political movements in Tamil Nadu > Narayana Guru": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Evolution of 19th and 20th century socio-political movements in Tamil Nadu",
        "subtopic": "Narayana Guru"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Evolution of 19th and 20th century socio-political movements in Tamil Nadu > Ayyankali": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Evolution of 19th and 20th century socio-political movements in Tamil Nadu",
        "subtopic": "Ayyankali"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Evolution of 19th and 20th century socio-political movements in Tamil Nadu > Vaikunda Swamigal": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Evolution of 19th and 20th century socio-political movements in Tamil Nadu",
        "subtopic": "Vaikunda Swamigal"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Justice Party > Dravidian Association": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Justice Party",
        "subtopic": "Dravidian Association"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Justice Party > South Indian Welfare Rights Association": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Justice Party",
        "subtopic": "South Indian Welfare Rights Association"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Justice Party > Non-Brahmin Conference": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Justice Party",
        "subtopic": "Non-Brahmin Conference"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Justice Party > Policies of the Justice Party": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Justice Party",
        "subtopic": "Policies of the Justice Party"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Justice Party > Madras Provincial Association": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Justice Party",
        "subtopic": "Madras Provincial Association"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Justice Party > Justice Party and the Home Rule Movement": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Justice Party",
        "subtopic": "Justice Party and the Home Rule Movement"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Justice Party > Justice Party Administration": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Justice Party",
        "subtopic": "Justice Party Administration"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Justice Party > Achievers (Reformists & Leaders)": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Justice Party",
        "subtopic": "Achievers (Reformists & Leaders)"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Self Respect Movement > Fifteen-Point Programme": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Self Respect Movement",
        "subtopic": "Fifteen-Point Programme"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Self Respect Movement > Self-Respect Movement Conferences": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Self Respect Movement",
        "subtopic": "Self-Respect Movement Conferences"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Self Respect Movement > Achievements of the Self-Respect Movement": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Self Respect Movement",
        "subtopic": "Achievements of the Self-Respect Movement"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Dravidian Movement > Rationalism, Social Reform & Dravidian Movement": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Dravidian Movement",
        "subtopic": "Rationalism, Social Reform & Dravidian Movement"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Contributions of Thanthai Periyar > Rationalism - Explanation": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Contributions of Thanthai Periyar",
        "subtopic": "Rationalism - Explanation"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Contributions of Thanthai Periyar > Women’s Liberation": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Contributions of Thanthai Periyar",
        "subtopic": "Women’s Liberation"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Contributions of Thanthai Periyar > Social Reform": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Contributions of Thanthai Periyar",
        "subtopic": "Social Reform"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Contributions of Thanthai Periyar > Vaikom Struggle": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Contributions of Thanthai Periyar",
        "subtopic": "Vaikom Struggle"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Contributions of Perarignar Anna > Annadurai’s Golden Sayings": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Contributions of Perarignar Anna",
        "subtopic": "Annadurai’s Golden Sayings"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Contributions of Perarignar Anna > Dravidar Kazhagam (DK)": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Contributions of Perarignar Anna",
        "subtopic": "Dravidar Kazhagam (DK)"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Contributions of Perarignar Anna > Founding of Dravida Munnetra Kazhagam (DMK)": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Contributions of Perarignar Anna",
        "subtopic": "Founding of Dravida Munnetra Kazhagam (DMK)"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Contributions of Perarignar Anna > Achievements of Annadurai as Chief Minister of Tamil Nadu": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Contributions of Perarignar Anna",
        "subtopic": "Achievements of Annadurai as Chief Minister of Tamil Nadu"
    },
    "History, Culture, Heritage & Socio-Political Movements in Tamilnadu > Contributions of Perarignar Anna > Annadurai’s Literary Works": {
        "subject": "History, Culture, Heritage & Socio-Political Movements in Tamilnadu",
        "topic": "Contributions of Perarignar Anna",
        "subtopic": "Annadurai’s Literary Works"
    },
    "Aptitude > Simplification > BODMAS": {
        "subject": "Aptitude",
        "topic": "Simplification",
        "subtopic": "BODMAS"
    },
    "Aptitude > Simplification > Powers": {
        "subject": "Aptitude",
        "topic": "Simplification",
        "subtopic": "Powers"
    },
    "Aptitude > Simplification > Surds & Indices": {
        "subject": "Aptitude",
        "topic": "Simplification",
        "subtopic": "Surds & Indices"
    },
    "Aptitude > Simplification > AP & GP": {
        "subject": "Aptitude",
        "topic": "Simplification",
        "subtopic": "AP & GP"
    },
    "Aptitude > Simplification > Special Series": {
        "subject": "Aptitude",
        "topic": "Simplification",
        "subtopic": "Special Series"
    },
    "Aptitude > Percentage > Percentage Increase and Decrease": {
        "subject": "Aptitude",
        "topic": "Percentage",
        "subtopic": "Percentage Increase and Decrease"
    },
    "Aptitude > Percentage > Exam and Marks Related Problems": {
        "subject": "Aptitude",
        "topic": "Percentage",
        "subtopic": "Exam and Marks Related Problems"
    },
    "Aptitude > Percentage > Population and Growth Problems": {
        "subject": "Aptitude",
        "topic": "Percentage",
        "subtopic": "Population and Growth Problems"
    },
    "Aptitude > Percentage > Profit and Loss": {
        "subject": "Aptitude",
        "topic": "Percentage",
        "subtopic": "Profit and Loss"
    },
    "Aptitude > Highest Common Factor (HCF) > Problems on Remainders": {
        "subject": "Aptitude",
        "topic": "Highest Common Factor (HCF)",
        "subtopic": "Problems on Remainders"
    },
    "Aptitude > Lowest Common Multiple (LCM) > problems on Multiples and Factors": {
        "subject": "Aptitude",
        "topic": "Lowest Common Multiple (LCM)",
        "subtopic": "problems on Multiples and Factors"
    },
    "Aptitude > Lowest Common Multiple (LCM) > Prime Factorization and Division Method Usage": {
        "subject": "Aptitude",
        "topic": "Lowest Common Multiple (LCM)",
        "subtopic": "Prime Factorization and Division Method Usage"
    },
    "Aptitude > Ratio and Proportion > Mixture and Alligation": {
        "subject": "Aptitude",
        "topic": "Ratio and Proportion",
        "subtopic": "Mixture and Alligation"
    },
    "Aptitude > Ratio and Proportion > Problems on Ages": {
        "subject": "Aptitude",
        "topic": "Ratio and Proportion",
        "subtopic": "Problems on Ages"
    },
    "Aptitude > Ratio and Proportion > Number System": {
        "subject": "Aptitude",
        "topic": "Ratio and Proportion",
        "subtopic": "Number System"
    },
    "Aptitude > Ratio and Proportion > Average": {
        "subject": "Aptitude",
        "topic": "Ratio and Proportion",
        "subtopic": "Average"
    },
    "Aptitude > Simple interest > Finding Total Amount, Principal, Interest, Time": {
        "subject": "Aptitude",
        "topic": "Simple interest",
        "subtopic": "Finding Total Amount, Principal, Interest, Time"
    },
    "Aptitude > Simple interest > Borrowing and Lending Problem": {
        "subject": "Aptitude",
        "topic": "Simple interest",
        "subtopic": "Borrowing and Lending Problem"
    },
    "Aptitude > Compound interest > Finding Total Amount, Principal, Interest, Time": {
        "subject": "Aptitude",
        "topic": "Compound interest",
        "subtopic": "Finding Total Amount, Principal, Interest, Time"
    },
    "Aptitude > Compound interest > Compound Interest When Interest is Compounded Half-Yearly or Quarterly": {
        "subject": "Aptitude",
        "topic": "Compound interest",
        "subtopic": "Compound Interest When Interest is Compounded Half-Yearly or Quarterly"
    },
    "Aptitude > Compound interest > Difference Between Simple Interest and Compound Interest": {
        "subject": "Aptitude",
        "topic": "Compound interest",
        "subtopic": "Difference Between Simple Interest and Compound Interest"
    },
    "Aptitude > Area > Square": {
        "subject": "Aptitude",
        "topic": "Area",
        "subtopic": "Square"
    },
    "Aptitude > Area > Rectangle": {
        "subject": "Aptitude",
        "topic": "Area",
        "subtopic": "Rectangle"
    },
    "Aptitude > Area > Triangle": {
        "subject": "Aptitude",
        "topic": "Area",
        "subtopic": "Triangle"
    },
    "Aptitude > Area > Circle": {
        "subject": "Aptitude",
        "topic": "Area",
        "subtopic": "Circle"
    },
    "Aptitude > Area > Parallelogram": {
        "subject": "Aptitude",
        "topic": "Area",
        "subtopic": "Parallelogram"
    },
    "Aptitude > Area > Trapezoid": {
        "subject": "Aptitude",
        "topic": "Area",
        "subtopic": "Trapezoid"
    },
    "Aptitude > Volume > Cube": {
        "subject": "Aptitude",
        "topic": "Volume",
        "subtopic": "Cube"
    },
    "Aptitude > Volume > Cuboid": {
        "subject": "Aptitude",
        "topic": "Volume",
        "subtopic": "Cuboid"
    },
    "Aptitude > Volume > Cone": {
        "subject": "Aptitude",
        "topic": "Volume",
        "subtopic": "Cone"
    },
    "Aptitude > Volume > Cylinder": {
        "subject": "Aptitude",
        "topic": "Volume",
        "subtopic": "Cylinder"
    },
    "Aptitude > Volume > Sphere": {
        "subject": "Aptitude",
        "topic": "Volume",
        "subtopic": "Sphere"
    },
    "Aptitude > Volume > Hemi Sphere": {
        "subject": "Aptitude",
        "topic": "Volume",
        "subtopic": "Hemi Sphere"
    },
    "Aptitude > Time and Work > Work Done by Multiple People Together": {
        "subject": "Aptitude",
        "topic": "Time and Work",
        "subtopic": "Work Done by Multiple People Together"
    },
    "Aptitude > Time and Work > Work and Efficiency Relationship": {
        "subject": "Aptitude",
        "topic": "Time and Work",
        "subtopic": "Work and Efficiency Relationship"
    },
    "Aptitude > Time and Work > Work Done by Alternating Workers": {
        "subject": "Aptitude",
        "topic": "Time and Work",
        "subtopic": "Work Done by Alternating Workers"
    },
    "Reasoning > Logical reasoning > seating arrangment": {
        "subject": "Reasoning",
        "topic": "Logical reasoning",
        "subtopic": "seating arrangment"
    },
    "Reasoning > Logical reasoning > Chronological order": {
        "subject": "Reasoning",
        "topic": "Logical reasoning",
        "subtopic": "Chronological order"
    },
    "Reasoning > Logical reasoning > syllogism": {
        "subject": "Reasoning",
        "topic": "Logical reasoning",
        "subtopic": "syllogism"
    },
    "Reasoning > Logical reasoning > Venn diagram": {
        "subject": "Reasoning",
        "topic": "Logical reasoning",
        "subtopic": "Venn diagram"
    },
    "Reasoning > Logical reasoning > Calander": {
        "subject": "Reasoning",
        "topic": "Logical reasoning",
        "subtopic": "Calander"
    },
    "Reasoning > Logical reasoning > Statement and Conclusions": {
        "subject": "Reasoning",
        "topic": "Logical reasoning",
        "subtopic": "Statement and Conclusions"
    },
    "Reasoning > Puzzles > Box Type Missing numbers": {
        "subject": "Reasoning",
        "topic": "Puzzles",
        "subtopic": "Box Type Missing numbers"
    },
    "Reasoning > Puzzles > Number of Triangle Etc": {
        "subject": "Reasoning",
        "topic": "Puzzles",
        "subtopic": "Number of Triangle Etc"
    },
    "Reasoning > Puzzles > Blood Relations": {
        "subject": "Reasoning",
        "topic": "Puzzles",
        "subtopic": "Blood Relations"
    },
    "Reasoning > Puzzles > Classification & Odd one out": {
        "subject": "Reasoning",
        "topic": "Puzzles",
        "subtopic": "Classification & Odd one out"
    },
    "Reasoning > Dice > Normal Dice": {
        "subject": "Reasoning",
        "topic": "Dice",
        "subtopic": "Normal Dice"
    },
    "Reasoning > Dice > Standard Dice": {
        "subject": "Reasoning",
        "topic": "Dice",
        "subtopic": "Standard Dice"
    },
    "Reasoning > Visual reasoning > Clock": {
        "subject": "Reasoning",
        "topic": "Visual reasoning",
        "subtopic": "Clock"
    },
    "Reasoning > Visual reasoning > Directions": {
        "subject": "Reasoning",
        "topic": "Visual reasoning",
        "subtopic": "Directions"
    },
    "Reasoning > Visual reasoning > Embeded figures": {
        "subject": "Reasoning",
        "topic": "Visual reasoning",
        "subtopic": "Embeded figures"
    },
    "Reasoning > Visual reasoning > Figural Classifications": {
        "subject": "Reasoning",
        "topic": "Visual reasoning",
        "subtopic": "Figural Classifications"
    },
    "Reasoning > Visual reasoning > Paper Cutting and Folding": {
        "subject": "Reasoning",
        "topic": "Visual reasoning",
        "subtopic": "Paper Cutting and Folding"
    },
    "Reasoning > Visual reasoning > Mirror iamge": {
        "subject": "Reasoning",
        "topic": "Visual reasoning",
        "subtopic": "Mirror iamge"
    },
    "Reasoning > Alpha numeric reasoning > Analogy": {
        "subject": "Reasoning",
        "topic": "Alpha numeric reasoning",
        "subtopic": "Analogy"
    },
    "Reasoning > Alpha numeric reasoning > Coding and decoding": {
        "subject": "Reasoning",
        "topic": "Alpha numeric reasoning",
        "subtopic": "Coding and decoding"
    },
    "Reasoning > Alpha numeric reasoning > Missing Letters": {
        "subject": "Reasoning",
        "topic": "Alpha numeric reasoning",
        "subtopic": "Missing Letters"
    },
    "Reasoning > Number series > Mathamatical Operations": {
        "subject": "Reasoning",
        "topic": "Number series",
        "subtopic": "Mathamatical Operations"
    },
    "Reasoning > Number series > Missing numbers": {
        "subject": "Reasoning",
        "topic": "Number series",
        "subtopic": "Missing numbers"
    },
    "Reasoning > Number series > Series complete": {
        "subject": "Reasoning",
        "topic": "Number series",
        "subtopic": "Series complete"
    },
}


# ===== BANKING TAXONOMY =====

BANKING_SUBJECTS: List[str] = [
    "Aptitude",
    "English",
    "Reasoning",
]

BANKING_TRIPLETS: List[str] = [
    "Reasoning > Seating Arrangement (Linear) > Facing North",
    "Reasoning > Seating Arrangement (Linear) > Facing South",
    "Reasoning > Seating Arrangement (Linear) > Facing North & South",
    "Reasoning > Seating Arrangement (Linear) > Unknown no. of persons",
    "Reasoning > Seating Arrangement (Linear) > Double row",
    "Reasoning > Seating Arrangement (Linear) > Triple row",
    "Reasoning > Seating Arrangement (Circular) > Facing Inside",
    "Reasoning > Seating Arrangement (Circular) > Facing Outside",
    "Reasoning > Seating Arrangement (Circular) > Facing inside & Outside",
    "Reasoning > Seating Arrangement (Circular) > Unknown no. of persons",
    "Reasoning > Seating Arrangement (Circular) > Concentric Circle",
    "Reasoning > Seating Arrangement (Square) > Facing Inside",
    "Reasoning > Seating Arrangement (Square) > Facing Outside",
    "Reasoning > Seating Arrangement (Square) > Facing inside & Outside",
    "Reasoning > Seating Arrangement (Square) > Concentric Square",
    "Reasoning > Seating Arrangement (Rectangle) > Facing Inside",
    "Reasoning > Seating Arrangement (Rectangle) > Facing Outside",
    "Reasoning > Seating Arrangement (Rectangle) > Facing inside & Outside",
    "Reasoning > Seating Arrangement (Rectangle) > Concentric rectangle",
    "Reasoning > Seating Arrangement (Triangular) > Facing Inside",
    "Reasoning > Seating Arrangement (Triangular) > Facing Outside",
    "Reasoning > Seating Arrangement (Triangular) > Facing inside & Outside",
    "Reasoning > Seating Arrangement (Triangular) > Concentric Triangle",
    "Reasoning > Seating Arrangement (Hexagonal) > Facing Inside",
    "Reasoning > Seating Arrangement (Hexagonal) > Facing Outside",
    "Reasoning > Seating Arrangement (Hexagonal) > Facing inside & Outside",
    "Reasoning > Seating Arrangement (Hexagonal) > Concentric",
    "Reasoning > Tabular Puzzles > Designation",
    "Reasoning > Tabular Puzzles > Days",
    "Reasoning > Tabular Puzzles > Month",
    "Reasoning > Tabular Puzzles > Month & Date",
    "Reasoning > Tabular Puzzles > Year & age",
    "Reasoning > Tabular Puzzles > Grouping",
    "Reasoning > Floor puzzles > Single floor",
    "Reasoning > Floor puzzles > Floor & Flat",
    "Reasoning > Floor puzzles > Unknown no. of Floor",
    "Reasoning > Box puzzles > Single stack",
    "Reasoning > Box puzzles > Stack 1 & Stack 2",
    "Reasoning > Box puzzles > Unknown no. of stack",
    "Reasoning > Other puzzles > Sequence based puzzle",
    "Reasoning > Other puzzles > Quantity based puzzle",
    "Reasoning > Other puzzles > Matrix based puzzle",
    "Reasoning > Other puzzles > Order & Ranking Puzzle",
    "Reasoning > Other puzzles > Pyramid Puzzle",
    "Reasoning > Coding-Decoding > Letter coding",
    "Reasoning > Coding-Decoding > Symbol digit coding",
    "Reasoning > Coding-Decoding > Coding in fictitious language",
    "Reasoning > Coding-Decoding > Coding based on condition",
    "Reasoning > Coding-Decoding > Problems based on new types: Letters; symbols and numbers;",
    "Reasoning > Coding-Decoding > Box type coding and decoding",
    "Reasoning > Directions > Normal",
    "Reasoning > Directions > Coded direction",
    "Reasoning > Blood relation > Normal",
    "Reasoning > Blood relation > Coded Blood relation",
    "Reasoning > Alphanumeric Symbol series > Number+Alphabets+Symbol series",
    "Reasoning > Alphanumeric Symbol series > Three/Four letter Word series",
    "Reasoning > Alphanumeric Symbol series > Three digit Number Series",
    "Reasoning > Alphanumeric Symbol series > Conditional ANS series",
    "Reasoning > Syllogism > Direct",
    "Reasoning > Syllogism > Coded",
    "Reasoning > Syllogism > Reverse",
    "Reasoning > Inequality > Direct",
    "Reasoning > Inequality > Coded",
    "Reasoning > Inequality > Reverse",
    "Reasoning > Inequality > Missing inequality",
    "Reasoning > Order and Ranking > Order and Ranking",
    "Reasoning > Numerical operations > Numerical operations",
    "Reasoning > Alphabetical operations > Alphabetical operations",
    "Reasoning > Pairs of letters > Pairs of letters",
    "Reasoning > Pairs of words > Pairs of words",
    "Reasoning > Meaningful words > Meaningful words",
    "Reasoning > Missing series > Missing series",
    "Reasoning > Odd one out > Odd one out",
    "Reasoning > Miscellaneous > Next series",
    "Reasoning > Miscellaneous > Miscellaneous",
    "Reasoning > Logical Reasoning > Statements and Arguments",
    "Reasoning > Logical Reasoning > Cause and Effect",
    "Reasoning > Logical Reasoning > Statements and Assumption",
    "Reasoning > Logical Reasoning > Statements and Course of Action",
    "Reasoning > Logical Reasoning > Statements and Conclusion",
    "Reasoning > Logical Reasoning > Statements and inferences",
    "Reasoning > Sequential Output Tracing > Numbers",
    "Reasoning > Sequential Output Tracing > Words",
    "Reasoning > Sequential Output Tracing > Numbers and words",
    "Reasoning > Sequential Output Tracing > Box type",
    "Reasoning > Statements - Data Sufficiency > 2 statements",
    "Reasoning > Statements - Data Sufficiency > 3 Statements",
    "Aptitude > Single Graph DI > DI Line",
    "Aptitude > Single Graph DI > DI Bar",
    "Aptitude > Single Graph DI > DI Table",
    "Aptitude > Single Graph DI > DI Pie",
    "Aptitude > Single Graph DI > DI Missing",
    "Aptitude > Single Graph DI > DI Radar",
    "Aptitude > Single Graph DI > DI Funnel",
    "Aptitude > Single Graph DI > DI Candle stick",
    "Aptitude > Single Graph DI > DI Caselet",
    "Aptitude > Mixed DI > DI Table + Pie",
    "Aptitude > Mixed DI > DI Table + Bar",
    "Aptitude > Mixed DI > DI Table + Line",
    "Aptitude > Mixed DI > Double Pie DI",
    "Aptitude > Mixed DI > Double Bar DI",
    "Aptitude > Mixed DI > Double Line DI",
    "Aptitude > Mixed DI > DI Pie + Line",
    "Aptitude > Mixed DI > DI Pie + Bar",
    "Aptitude > Mixed DI > DI line + Bar",
    "Aptitude > Mixed DI > DI Graph with Note",
    "Aptitude > Application DI > Arithematic question based DI",
    "Aptitude > Missing Number > Single series",
    "Aptitude > Missing Number > Double series with statement",
    "Aptitude > Missing Number > Triple series with statement",
    "Aptitude > Missing Number > Single series with Quadratic equation",
    "Aptitude > Wrong Number > Single series",
    "Aptitude > Wrong Number > Double series with statement",
    "Aptitude > Wrong Number > Triple series with statement",
    "Aptitude > Quadratic Equation > Linear Equation",
    "Aptitude > Quadratic Equation > Quadratic Equation with Coefficient",
    "Aptitude > Quadratic Equation > Quadratic Equation with out Coefficient",
    "Aptitude > Quadratic Equation > New pattern QE",
    "Aptitude > Simplification and Approximation > Simplification",
    "Aptitude > Simplification and Approximation > Approximation",
    "Aptitude > Quantity Comparision > Quantity I & II (All Arithmetic topic)",
    "Aptitude > Data sufficiency > 2 statement (All Arithmetic topic)",
    "Aptitude > Data sufficiency > 3 Statement (All Arithmetic topic)",
    "Aptitude > Ratio Proportion > Statement Question",
    "Aptitude > Ratio Proportion > Passage based Question",
    "Aptitude > Ratio Proportion > Double filler question",
    "Aptitude > Average > Statement Question",
    "Aptitude > Average > Passage based Question",
    "Aptitude > Average > Double filler question",
    "Aptitude > Percentage > Statement Question",
    "Aptitude > Percentage > Passage based Question",
    "Aptitude > Percentage > Double filler question",
    "Aptitude > Ages > Statement Question",
    "Aptitude > Ages > Passage based Question",
    "Aptitude > Ages > Double filler question",
    "Aptitude > Partnership > Statement Question",
    "Aptitude > Partnership > Passage based Question",
    "Aptitude > Partnership > Double filler question",
    "Aptitude > Profit & Loss > Statement Question",
    "Aptitude > Profit & Loss > Passage based Question",
    "Aptitude > Profit & Loss > Double filler question",
    "Aptitude > Time Speed Distance > Statement Question",
    "Aptitude > Time Speed Distance > Passage based Question",
    "Aptitude > Time Speed Distance > Double filler question",
    "Aptitude > Problems on Trains > Statement Question",
    "Aptitude > Problems on Trains > Passage based Question",
    "Aptitude > Problems on Trains > Double filler question",
    "Aptitude > Boats & Stream > Statement Question",
    "Aptitude > Boats & Stream > Passage based Question",
    "Aptitude > Boats & Stream > Double filler question",
    "Aptitude > Time & Work > Statement Question",
    "Aptitude > Time & Work > Passage based Question",
    "Aptitude > Time & Work > Double filler question",
    "Aptitude > Pipes & Cistern > Statement Question",
    "Aptitude > Pipes & Cistern > Passage based Question",
    "Aptitude > Pipes & Cistern > Double filler question",
    "Aptitude > Simple Interest > Statement Question",
    "Aptitude > Simple Interest > Passage based Question",
    "Aptitude > Simple Interest > Double filler question",
    "Aptitude > Compound Interest > Statement Question",
    "Aptitude > Compound Interest > Passage based Question",
    "Aptitude > Compound Interest > Double filler question",
    "Aptitude > Mixtures & Alligations > Statement Question",
    "Aptitude > Mixtures & Alligations > Passage based Question",
    "Aptitude > Mixtures & Alligations > Double filler question",
    "Aptitude > Permutation & Combination > Statement Question",
    "Aptitude > Permutation & Combination > Passage based Question",
    "Aptitude > Permutation & Combination > Double filler question",
    "Aptitude > Probability > Statement Question",
    "Aptitude > Probability > Passage based Question",
    "Aptitude > Probability > Double filler question",
    "Aptitude > Miscellaneous > Miscellaneous",
    "English > Reading Comprehension > Analytical passage",
    "English > Reading Comprehension > Informative passage",
    "English > Reading Comprehension > Banking and Economy",
    "English > Reading Comprehension > Story-based passage",
    "English > Reading Comprehension > Technology",
    "English > Reading Comprehension > Research-based",
    "English > Reading Comprehension > Health and Self-improvement",
    "English > Parajumble > Basic para jumble",
    "English > Parajumble > Para jumble with exclusion or inclusion",
    "English > Parajumble > Para jumble with error spotting",
    "English > Parajumble > Para jumble with rearrangement",
    "English > Parajumble > Para jumble with a blank",
    "English > Parajumble > Para jumble with match the columns",
    "English > Parajumble > Para jumble with phrasal filler",
    "English > Parajumble > Para jumble with a fixed sentence",
    "English > Sentence Rearrangement > Rearrangement with four/five parts",
    "English > Sentence Rearrangement > Omission of irrelevant part",
    "English > Match the columns > Basic pattern with two or three columns",
    "English > Match the columns > Match the column with the connector",
    "English > Match the columns > Columns with fillers or word swap",
    "English > Match the columns > Columns with error spotting",
    "English > Match the columns > Match the column with column fillers",
    "English > Statement based > Para completion",
    "English > Statement based > Paragraph inference or cause",
    "English > Statement based > odd one out from the theme",
    "English > Error Spotting > Correct sentence",
    "English > Error Spotting > Incorrect sentence",
    "English > Error Spotting > Number of errors in a sentence",
    "English > Error Spotting > Error parts in a sentence",
    "English > Error Spotting > Error-free parts in a sentence",
    "English > Phrasal replacement > Phrasal verb replacement",
    "English > Phrasal replacement > Phrase replacement",
    "English > Phrasal replacement > Choose the correct meaning of the highlighted phrase",
    "English > Cloze test > Basic type",
    "English > Cloze test > Blanks followed by a synonym",
    "English > Cloze test > Two or three options for a single blank",
    "English > Cloze test > Inappropriate option for the blank",
    "English > Cloze test > Blanks to be filled by a phrase or phrasal verb",
    "English > Fill in the blanks > Single filler",
    "English > Fill in the blanks > Double filler",
    "English > Fill in the blanks > Triple filler",
    "English > Word Usage > Usage of words",
    "English > Word Swap > Word swap in a sentence",
    "English > Word Swap > Word swap in a passage",
    "English > Word Swap > Word swap with inappropriate word",
    "English > Mis-spelt > Spelling error",
    "English > Mis-spelt > Inappropriate words",
    "English > Synonyms & Antonyms > Synonyms",
    "English > Synonyms & Antonyms > Antonyms",
    "English > Idioms > Meaning of the idioms",
    "English > Idioms > Meaning of the phrases",
    "English > Idioms > Fillers with Idioms",
    "English > Idioms > Fillers with Phrasal verbs",
    "English > Idioms > Similar usage of the Idiom",
    "English > Idioms > Similar usage of the phrase",
    "English > Connectors/starters > Grammar-based",
    "English > Connectors/starters > Context-based",
    "Reasoning > Direction > Normal",
    "Reasoning > Direction > Coded direction",
    "Reasoning > Meaningful words > Meaningful word",
]

BANKING_TRIPLET_DICT: Dict[str, Dict[str, str]] = {
    "Reasoning > Seating Arrangement (Linear) > Facing North": {
        "subject": "Reasoning",
        "topic": "Seating Arrangement (Linear)",
        "subtopic": "Facing North"
    },
    "Reasoning > Seating Arrangement (Linear) > Facing South": {
        "subject": "Reasoning",
        "topic": "Seating Arrangement (Linear)",
        "subtopic": "Facing South"
    },
    "Reasoning > Seating Arrangement (Linear) > Facing North & South": {
        "subject": "Reasoning",
        "topic": "Seating Arrangement (Linear)",
        "subtopic": "Facing North & South"
    },
    "Reasoning > Seating Arrangement (Linear) > Unknown no. of persons": {
        "subject": "Reasoning",
        "topic": "Seating Arrangement (Linear)",
        "subtopic": "Unknown no. of persons"
    },
    "Reasoning > Seating Arrangement (Linear) > Double row": {
        "subject": "Reasoning",
        "topic": "Seating Arrangement (Linear)",
        "subtopic": "Double row"
    },
    "Reasoning > Seating Arrangement (Linear) > Triple row": {
        "subject": "Reasoning",
        "topic": "Seating Arrangement (Linear)",
        "subtopic": "Triple row"
    },
    "Reasoning > Seating Arrangement (Circular) > Facing Inside": {
        "subject": "Reasoning",
        "topic": "Seating Arrangement (Circular)",
        "subtopic": "Facing Inside"
    },
    "Reasoning > Seating Arrangement (Circular) > Facing Outside": {
        "subject": "Reasoning",
        "topic": "Seating Arrangement (Circular)",
        "subtopic": "Facing Outside"
    },
    "Reasoning > Seating Arrangement (Circular) > Facing inside & Outside": {
        "subject": "Reasoning",
        "topic": "Seating Arrangement (Circular)",
        "subtopic": "Facing inside & Outside"
    },
    "Reasoning > Seating Arrangement (Circular) > Unknown no. of persons": {
        "subject": "Reasoning",
        "topic": "Seating Arrangement (Circular)",
        "subtopic": "Unknown no. of persons"
    },
    "Reasoning > Seating Arrangement (Circular) > Concentric Circle": {
        "subject": "Reasoning",
        "topic": "Seating Arrangement (Circular)",
        "subtopic": "Concentric Circle"
    },
    "Reasoning > Seating Arrangement (Square) > Facing Inside": {
        "subject": "Reasoning",
        "topic": "Seating Arrangement (Square)",
        "subtopic": "Facing Inside"
    },
    "Reasoning > Seating Arrangement (Square) > Facing Outside": {
        "subject": "Reasoning",
        "topic": "Seating Arrangement (Square)",
        "subtopic": "Facing Outside"
    },
    "Reasoning > Seating Arrangement (Square) > Facing inside & Outside": {
        "subject": "Reasoning",
        "topic": "Seating Arrangement (Square)",
        "subtopic": "Facing inside & Outside"
    },
    "Reasoning > Seating Arrangement (Square) > Concentric Square": {
        "subject": "Reasoning",
        "topic": "Seating Arrangement (Square)",
        "subtopic": "Concentric Square"
    },
    "Reasoning > Seating Arrangement (Rectangle) > Facing Inside": {
        "subject": "Reasoning",
        "topic": "Seating Arrangement (Rectangle)",
        "subtopic": "Facing Inside"
    },
    "Reasoning > Seating Arrangement (Rectangle) > Facing Outside": {
        "subject": "Reasoning",
        "topic": "Seating Arrangement (Rectangle)",
        "subtopic": "Facing Outside"
    },
    "Reasoning > Seating Arrangement (Rectangle) > Facing inside & Outside": {
        "subject": "Reasoning",
        "topic": "Seating Arrangement (Rectangle)",
        "subtopic": "Facing inside & Outside"
    },
    "Reasoning > Seating Arrangement (Rectangle) > Concentric rectangle": {
        "subject": "Reasoning",
        "topic": "Seating Arrangement (Rectangle)",
        "subtopic": "Concentric rectangle"
    },
    "Reasoning > Seating Arrangement (Triangular) > Facing Inside": {
        "subject": "Reasoning",
        "topic": "Seating Arrangement (Triangular)",
        "subtopic": "Facing Inside"
    },
    "Reasoning > Seating Arrangement (Triangular) > Facing Outside": {
        "subject": "Reasoning",
        "topic": "Seating Arrangement (Triangular)",
        "subtopic": "Facing Outside"
    },
    "Reasoning > Seating Arrangement (Triangular) > Facing inside & Outside": {
        "subject": "Reasoning",
        "topic": "Seating Arrangement (Triangular)",
        "subtopic": "Facing inside & Outside"
    },
    "Reasoning > Seating Arrangement (Triangular) > Concentric Triangle": {
        "subject": "Reasoning",
        "topic": "Seating Arrangement (Triangular)",
        "subtopic": "Concentric Triangle"
    },
    "Reasoning > Seating Arrangement (Hexagonal) > Facing Inside": {
        "subject": "Reasoning",
        "topic": "Seating Arrangement (Hexagonal)",
        "subtopic": "Facing Inside"
    },
    "Reasoning > Seating Arrangement (Hexagonal) > Facing Outside": {
        "subject": "Reasoning",
        "topic": "Seating Arrangement (Hexagonal)",
        "subtopic": "Facing Outside"
    },
    "Reasoning > Seating Arrangement (Hexagonal) > Facing inside & Outside": {
        "subject": "Reasoning",
        "topic": "Seating Arrangement (Hexagonal)",
        "subtopic": "Facing inside & Outside"
    },
    "Reasoning > Seating Arrangement (Hexagonal) > Concentric": {
        "subject": "Reasoning",
        "topic": "Seating Arrangement (Hexagonal)",
        "subtopic": "Concentric"
    },
    "Reasoning > Tabular Puzzles > Designation": {
        "subject": "Reasoning",
        "topic": "Tabular Puzzles",
        "subtopic": "Designation"
    },
    "Reasoning > Tabular Puzzles > Days": {
        "subject": "Reasoning",
        "topic": "Tabular Puzzles",
        "subtopic": "Days"
    },
    "Reasoning > Tabular Puzzles > Month": {
        "subject": "Reasoning",
        "topic": "Tabular Puzzles",
        "subtopic": "Month"
    },
    "Reasoning > Tabular Puzzles > Month & Date": {
        "subject": "Reasoning",
        "topic": "Tabular Puzzles",
        "subtopic": "Month & Date"
    },
    "Reasoning > Tabular Puzzles > Year & age": {
        "subject": "Reasoning",
        "topic": "Tabular Puzzles",
        "subtopic": "Year & age"
    },
    "Reasoning > Tabular Puzzles > Grouping": {
        "subject": "Reasoning",
        "topic": "Tabular Puzzles",
        "subtopic": "Grouping"
    },
    "Reasoning > Floor puzzles > Single floor": {
        "subject": "Reasoning",
        "topic": "Floor puzzles",
        "subtopic": "Single floor"
    },
    "Reasoning > Floor puzzles > Floor & Flat": {
        "subject": "Reasoning",
        "topic": "Floor puzzles",
        "subtopic": "Floor & Flat"
    },
    "Reasoning > Floor puzzles > Unknown no. of Floor": {
        "subject": "Reasoning",
        "topic": "Floor puzzles",
        "subtopic": "Unknown no. of Floor"
    },
    "Reasoning > Box puzzles > Single stack": {
        "subject": "Reasoning",
        "topic": "Box puzzles",
        "subtopic": "Single stack"
    },
    "Reasoning > Box puzzles > Stack 1 & Stack 2": {
        "subject": "Reasoning",
        "topic": "Box puzzles",
        "subtopic": "Stack 1 & Stack 2"
    },
    "Reasoning > Box puzzles > Unknown no. of stack": {
        "subject": "Reasoning",
        "topic": "Box puzzles",
        "subtopic": "Unknown no. of stack"
    },
    "Reasoning > Other puzzles > Sequence based puzzle": {
        "subject": "Reasoning",
        "topic": "Other puzzles",
        "subtopic": "Sequence based puzzle"
    },
    "Reasoning > Other puzzles > Quantity based puzzle": {
        "subject": "Reasoning",
        "topic": "Other puzzles",
        "subtopic": "Quantity based puzzle"
    },
    "Reasoning > Other puzzles > Matrix based puzzle": {
        "subject": "Reasoning",
        "topic": "Other puzzles",
        "subtopic": "Matrix based puzzle"
    },
    "Reasoning > Other puzzles > Order & Ranking Puzzle": {
        "subject": "Reasoning",
        "topic": "Other puzzles",
        "subtopic": "Order & Ranking Puzzle"
    },
    "Reasoning > Other puzzles > Pyramid Puzzle": {
        "subject": "Reasoning",
        "topic": "Other puzzles",
        "subtopic": "Pyramid Puzzle"
    },
    "Reasoning > Coding-Decoding > Letter coding": {
        "subject": "Reasoning",
        "topic": "Coding-Decoding",
        "subtopic": "Letter coding"
    },
    "Reasoning > Coding-Decoding > Symbol digit coding": {
        "subject": "Reasoning",
        "topic": "Coding-Decoding",
        "subtopic": "Symbol digit coding"
    },
    "Reasoning > Coding-Decoding > Coding in fictitious language": {
        "subject": "Reasoning",
        "topic": "Coding-Decoding",
        "subtopic": "Coding in fictitious language"
    },
    "Reasoning > Coding-Decoding > Coding based on condition": {
        "subject": "Reasoning",
        "topic": "Coding-Decoding",
        "subtopic": "Coding based on condition"
    },
    "Reasoning > Coding-Decoding > Problems based on new types: Letters; symbols and numbers;": {
        "subject": "Reasoning",
        "topic": "Coding-Decoding",
        "subtopic": "Problems based on new types: Letters; symbols and numbers;"
    },
    "Reasoning > Coding-Decoding > Box type coding and decoding": {
        "subject": "Reasoning",
        "topic": "Coding-Decoding",
        "subtopic": "Box type coding and decoding"
    },
    "Reasoning > Directions > Normal": {
        "subject": "Reasoning",
        "topic": "Directions",
        "subtopic": "Normal"
    },
    "Reasoning > Directions > Coded direction": {
        "subject": "Reasoning",
        "topic": "Directions",
        "subtopic": "Coded direction"
    },
    "Reasoning > Blood relation > Normal": {
        "subject": "Reasoning",
        "topic": "Blood relation",
        "subtopic": "Normal"
    },
    "Reasoning > Blood relation > Coded Blood relation": {
        "subject": "Reasoning",
        "topic": "Blood relation",
        "subtopic": "Coded Blood relation"
    },
    "Reasoning > Alphanumeric Symbol series > Number+Alphabets+Symbol series": {
        "subject": "Reasoning",
        "topic": "Alphanumeric Symbol series",
        "subtopic": "Number+Alphabets+Symbol series"
    },
    "Reasoning > Alphanumeric Symbol series > Three/Four letter Word series": {
        "subject": "Reasoning",
        "topic": "Alphanumeric Symbol series",
        "subtopic": "Three/Four letter Word series"
    },
    "Reasoning > Alphanumeric Symbol series > Three digit Number Series": {
        "subject": "Reasoning",
        "topic": "Alphanumeric Symbol series",
        "subtopic": "Three digit Number Series"
    },
    "Reasoning > Alphanumeric Symbol series > Conditional ANS series": {
        "subject": "Reasoning",
        "topic": "Alphanumeric Symbol series",
        "subtopic": "Conditional ANS series"
    },
    "Reasoning > Syllogism > Direct": {
        "subject": "Reasoning",
        "topic": "Syllogism",
        "subtopic": "Direct"
    },
    "Reasoning > Syllogism > Coded": {
        "subject": "Reasoning",
        "topic": "Syllogism",
        "subtopic": "Coded"
    },
    "Reasoning > Syllogism > Reverse": {
        "subject": "Reasoning",
        "topic": "Syllogism",
        "subtopic": "Reverse"
    },
    "Reasoning > Inequality > Direct": {
        "subject": "Reasoning",
        "topic": "Inequality",
        "subtopic": "Direct"
    },
    "Reasoning > Inequality > Coded": {
        "subject": "Reasoning",
        "topic": "Inequality",
        "subtopic": "Coded"
    },
    "Reasoning > Inequality > Reverse": {
        "subject": "Reasoning",
        "topic": "Inequality",
        "subtopic": "Reverse"
    },
    "Reasoning > Inequality > Missing inequality": {
        "subject": "Reasoning",
        "topic": "Inequality",
        "subtopic": "Missing inequality"
    },
    "Reasoning > Order and Ranking > Order and Ranking": {
        "subject": "Reasoning",
        "topic": "Order and Ranking",
        "subtopic": "Order and Ranking"
    },
    "Reasoning > Numerical operations > Numerical operations": {
        "subject": "Reasoning",
        "topic": "Numerical operations",
        "subtopic": "Numerical operations"
    },
    "Reasoning > Alphabetical operations > Alphabetical operations": {
        "subject": "Reasoning",
        "topic": "Alphabetical operations",
        "subtopic": "Alphabetical operations"
    },
    "Reasoning > Pairs of letters > Pairs of letters": {
        "subject": "Reasoning",
        "topic": "Pairs of letters",
        "subtopic": "Pairs of letters"
    },
    "Reasoning > Pairs of words > Pairs of words": {
        "subject": "Reasoning",
        "topic": "Pairs of words",
        "subtopic": "Pairs of words"
    },
    "Reasoning > Meaningful words > Meaningful words": {
        "subject": "Reasoning",
        "topic": "Meaningful words",
        "subtopic": "Meaningful words"
    },
    "Reasoning > Missing series > Missing series": {
        "subject": "Reasoning",
        "topic": "Missing series",
        "subtopic": "Missing series"
    },
    "Reasoning > Odd one out > Odd one out": {
        "subject": "Reasoning",
        "topic": "Odd one out",
        "subtopic": "Odd one out"
    },
    "Reasoning > Miscellaneous > Next series": {
        "subject": "Reasoning",
        "topic": "Miscellaneous",
        "subtopic": "Next series"
    },
    "Reasoning > Miscellaneous > Miscellaneous": {
        "subject": "Reasoning",
        "topic": "Miscellaneous",
        "subtopic": "Miscellaneous"
    },
    "Reasoning > Logical Reasoning > Statements and Arguments": {
        "subject": "Reasoning",
        "topic": "Logical Reasoning",
        "subtopic": "Statements and Arguments"
    },
    "Reasoning > Logical Reasoning > Cause and Effect": {
        "subject": "Reasoning",
        "topic": "Logical Reasoning",
        "subtopic": "Cause and Effect"
    },
    "Reasoning > Logical Reasoning > Statements and Assumption": {
        "subject": "Reasoning",
        "topic": "Logical Reasoning",
        "subtopic": "Statements and Assumption"
    },
    "Reasoning > Logical Reasoning > Statements and Course of Action": {
        "subject": "Reasoning",
        "topic": "Logical Reasoning",
        "subtopic": "Statements and Course of Action"
    },
    "Reasoning > Logical Reasoning > Statements and Conclusion": {
        "subject": "Reasoning",
        "topic": "Logical Reasoning",
        "subtopic": "Statements and Conclusion"
    },
    "Reasoning > Logical Reasoning > Statements and inferences": {
        "subject": "Reasoning",
        "topic": "Logical Reasoning",
        "subtopic": "Statements and inferences"
    },
    "Reasoning > Sequential Output Tracing > Numbers": {
        "subject": "Reasoning",
        "topic": "Sequential Output Tracing",
        "subtopic": "Numbers"
    },
    "Reasoning > Sequential Output Tracing > Words": {
        "subject": "Reasoning",
        "topic": "Sequential Output Tracing",
        "subtopic": "Words"
    },
    "Reasoning > Sequential Output Tracing > Numbers and words": {
        "subject": "Reasoning",
        "topic": "Sequential Output Tracing",
        "subtopic": "Numbers and words"
    },
    "Reasoning > Sequential Output Tracing > Box type": {
        "subject": "Reasoning",
        "topic": "Sequential Output Tracing",
        "subtopic": "Box type"
    },
    "Reasoning > Statements - Data Sufficiency > 2 statements": {
        "subject": "Reasoning",
        "topic": "Statements - Data Sufficiency",
        "subtopic": "2 statements"
    },
    "Reasoning > Statements - Data Sufficiency > 3 Statements": {
        "subject": "Reasoning",
        "topic": "Statements - Data Sufficiency",
        "subtopic": "3 Statements"
    },
    "Aptitude > Single Graph DI > DI Line": {
        "subject": "Aptitude",
        "topic": "Single Graph DI",
        "subtopic": "DI Line"
    },
    "Aptitude > Single Graph DI > DI Bar": {
        "subject": "Aptitude",
        "topic": "Single Graph DI",
        "subtopic": "DI Bar"
    },
    "Aptitude > Single Graph DI > DI Table": {
        "subject": "Aptitude",
        "topic": "Single Graph DI",
        "subtopic": "DI Table"
    },
    "Aptitude > Single Graph DI > DI Pie": {
        "subject": "Aptitude",
        "topic": "Single Graph DI",
        "subtopic": "DI Pie"
    },
    "Aptitude > Single Graph DI > DI Missing": {
        "subject": "Aptitude",
        "topic": "Single Graph DI",
        "subtopic": "DI Missing"
    },
    "Aptitude > Single Graph DI > DI Radar": {
        "subject": "Aptitude",
        "topic": "Single Graph DI",
        "subtopic": "DI Radar"
    },
    "Aptitude > Single Graph DI > DI Funnel": {
        "subject": "Aptitude",
        "topic": "Single Graph DI",
        "subtopic": "DI Funnel"
    },
    "Aptitude > Single Graph DI > DI Candle stick": {
        "subject": "Aptitude",
        "topic": "Single Graph DI",
        "subtopic": "DI Candle stick"
    },
    "Aptitude > Single Graph DI > DI Caselet": {
        "subject": "Aptitude",
        "topic": "Single Graph DI",
        "subtopic": "DI Caselet"
    },
    "Aptitude > Mixed DI > DI Table + Pie": {
        "subject": "Aptitude",
        "topic": "Mixed DI",
        "subtopic": "DI Table + Pie"
    },
    "Aptitude > Mixed DI > DI Table + Bar": {
        "subject": "Aptitude",
        "topic": "Mixed DI",
        "subtopic": "DI Table + Bar"
    },
    "Aptitude > Mixed DI > DI Table + Line": {
        "subject": "Aptitude",
        "topic": "Mixed DI",
        "subtopic": "DI Table + Line"
    },
    "Aptitude > Mixed DI > Double Pie DI": {
        "subject": "Aptitude",
        "topic": "Mixed DI",
        "subtopic": "Double Pie DI"
    },
    "Aptitude > Mixed DI > Double Bar DI": {
        "subject": "Aptitude",
        "topic": "Mixed DI",
        "subtopic": "Double Bar DI"
    },
    "Aptitude > Mixed DI > Double Line DI": {
        "subject": "Aptitude",
        "topic": "Mixed DI",
        "subtopic": "Double Line DI"
    },
    "Aptitude > Mixed DI > DI Pie + Line": {
        "subject": "Aptitude",
        "topic": "Mixed DI",
        "subtopic": "DI Pie + Line"
    },
    "Aptitude > Mixed DI > DI Pie + Bar": {
        "subject": "Aptitude",
        "topic": "Mixed DI",
        "subtopic": "DI Pie + Bar"
    },
    "Aptitude > Mixed DI > DI line + Bar": {
        "subject": "Aptitude",
        "topic": "Mixed DI",
        "subtopic": "DI line + Bar"
    },
    "Aptitude > Mixed DI > DI Graph with Note": {
        "subject": "Aptitude",
        "topic": "Mixed DI",
        "subtopic": "DI Graph with Note"
    },
    "Aptitude > Application DI > Arithematic question based DI": {
        "subject": "Aptitude",
        "topic": "Application DI",
        "subtopic": "Arithematic question based DI"
    },
    "Aptitude > Missing Number > Single series": {
        "subject": "Aptitude",
        "topic": "Missing Number",
        "subtopic": "Single series"
    },
    "Aptitude > Missing Number > Double series with statement": {
        "subject": "Aptitude",
        "topic": "Missing Number",
        "subtopic": "Double series with statement"
    },
    "Aptitude > Missing Number > Triple series with statement": {
        "subject": "Aptitude",
        "topic": "Missing Number",
        "subtopic": "Triple series with statement"
    },
    "Aptitude > Missing Number > Single series with Quadratic equation": {
        "subject": "Aptitude",
        "topic": "Missing Number",
        "subtopic": "Single series with Quadratic equation"
    },
    "Aptitude > Wrong Number > Single series": {
        "subject": "Aptitude",
        "topic": "Wrong Number",
        "subtopic": "Single series"
    },
    "Aptitude > Wrong Number > Double series with statement": {
        "subject": "Aptitude",
        "topic": "Wrong Number",
        "subtopic": "Double series with statement"
    },
    "Aptitude > Wrong Number > Triple series with statement": {
        "subject": "Aptitude",
        "topic": "Wrong Number",
        "subtopic": "Triple series with statement"
    },
    "Aptitude > Quadratic Equation > Linear Equation": {
        "subject": "Aptitude",
        "topic": "Quadratic Equation",
        "subtopic": "Linear Equation"
    },
    "Aptitude > Quadratic Equation > Quadratic Equation with Coefficient": {
        "subject": "Aptitude",
        "topic": "Quadratic Equation",
        "subtopic": "Quadratic Equation with Coefficient"
    },
    "Aptitude > Quadratic Equation > Quadratic Equation with out Coefficient": {
        "subject": "Aptitude",
        "topic": "Quadratic Equation",
        "subtopic": "Quadratic Equation with out Coefficient"
    },
    "Aptitude > Quadratic Equation > New pattern QE": {
        "subject": "Aptitude",
        "topic": "Quadratic Equation",
        "subtopic": "New pattern QE"
    },
    "Aptitude > Simplification and Approximation > Simplification": {
        "subject": "Aptitude",
        "topic": "Simplification and Approximation",
        "subtopic": "Simplification"
    },
    "Aptitude > Simplification and Approximation > Approximation": {
        "subject": "Aptitude",
        "topic": "Simplification and Approximation",
        "subtopic": "Approximation"
    },
    "Aptitude > Quantity Comparision > Quantity I & II (All Arithmetic topic)": {
        "subject": "Aptitude",
        "topic": "Quantity Comparision",
        "subtopic": "Quantity I & II (All Arithmetic topic)"
    },
    "Aptitude > Data sufficiency > 2 statement (All Arithmetic topic)": {
        "subject": "Aptitude",
        "topic": "Data sufficiency",
        "subtopic": "2 statement (All Arithmetic topic)"
    },
    "Aptitude > Data sufficiency > 3 Statement (All Arithmetic topic)": {
        "subject": "Aptitude",
        "topic": "Data sufficiency",
        "subtopic": "3 Statement (All Arithmetic topic)"
    },
    "Aptitude > Ratio Proportion > Statement Question": {
        "subject": "Aptitude",
        "topic": "Ratio Proportion",
        "subtopic": "Statement Question"
    },
    "Aptitude > Ratio Proportion > Passage based Question": {
        "subject": "Aptitude",
        "topic": "Ratio Proportion",
        "subtopic": "Passage based Question"
    },
    "Aptitude > Ratio Proportion > Double filler question": {
        "subject": "Aptitude",
        "topic": "Ratio Proportion",
        "subtopic": "Double filler question"
    },
    "Aptitude > Average > Statement Question": {
        "subject": "Aptitude",
        "topic": "Average",
        "subtopic": "Statement Question"
    },
    "Aptitude > Average > Passage based Question": {
        "subject": "Aptitude",
        "topic": "Average",
        "subtopic": "Passage based Question"
    },
    "Aptitude > Average > Double filler question": {
        "subject": "Aptitude",
        "topic": "Average",
        "subtopic": "Double filler question"
    },
    "Aptitude > Percentage > Statement Question": {
        "subject": "Aptitude",
        "topic": "Percentage",
        "subtopic": "Statement Question"
    },
    "Aptitude > Percentage > Passage based Question": {
        "subject": "Aptitude",
        "topic": "Percentage",
        "subtopic": "Passage based Question"
    },
    "Aptitude > Percentage > Double filler question": {
        "subject": "Aptitude",
        "topic": "Percentage",
        "subtopic": "Double filler question"
    },
    "Aptitude > Ages > Statement Question": {
        "subject": "Aptitude",
        "topic": "Ages",
        "subtopic": "Statement Question"
    },
    "Aptitude > Ages > Passage based Question": {
        "subject": "Aptitude",
        "topic": "Ages",
        "subtopic": "Passage based Question"
    },
    "Aptitude > Ages > Double filler question": {
        "subject": "Aptitude",
        "topic": "Ages",
        "subtopic": "Double filler question"
    },
    "Aptitude > Partnership > Statement Question": {
        "subject": "Aptitude",
        "topic": "Partnership",
        "subtopic": "Statement Question"
    },
    "Aptitude > Partnership > Passage based Question": {
        "subject": "Aptitude",
        "topic": "Partnership",
        "subtopic": "Passage based Question"
    },
    "Aptitude > Partnership > Double filler question": {
        "subject": "Aptitude",
        "topic": "Partnership",
        "subtopic": "Double filler question"
    },
    "Aptitude > Profit & Loss > Statement Question": {
        "subject": "Aptitude",
        "topic": "Profit & Loss",
        "subtopic": "Statement Question"
    },
    "Aptitude > Profit & Loss > Passage based Question": {
        "subject": "Aptitude",
        "topic": "Profit & Loss",
        "subtopic": "Passage based Question"
    },
    "Aptitude > Profit & Loss > Double filler question": {
        "subject": "Aptitude",
        "topic": "Profit & Loss",
        "subtopic": "Double filler question"
    },
    "Aptitude > Time Speed Distance > Statement Question": {
        "subject": "Aptitude",
        "topic": "Time Speed Distance",
        "subtopic": "Statement Question"
    },
    "Aptitude > Time Speed Distance > Passage based Question": {
        "subject": "Aptitude",
        "topic": "Time Speed Distance",
        "subtopic": "Passage based Question"
    },
    "Aptitude > Time Speed Distance > Double filler question": {
        "subject": "Aptitude",
        "topic": "Time Speed Distance",
        "subtopic": "Double filler question"
    },
    "Aptitude > Problems on Trains > Statement Question": {
        "subject": "Aptitude",
        "topic": "Problems on Trains",
        "subtopic": "Statement Question"
    },
    "Aptitude > Problems on Trains > Passage based Question": {
        "subject": "Aptitude",
        "topic": "Problems on Trains",
        "subtopic": "Passage based Question"
    },
    "Aptitude > Problems on Trains > Double filler question": {
        "subject": "Aptitude",
        "topic": "Problems on Trains",
        "subtopic": "Double filler question"
    },
    "Aptitude > Boats & Stream > Statement Question": {
        "subject": "Aptitude",
        "topic": "Boats & Stream",
        "subtopic": "Statement Question"
    },
    "Aptitude > Boats & Stream > Passage based Question": {
        "subject": "Aptitude",
        "topic": "Boats & Stream",
        "subtopic": "Passage based Question"
    },
    "Aptitude > Boats & Stream > Double filler question": {
        "subject": "Aptitude",
        "topic": "Boats & Stream",
        "subtopic": "Double filler question"
    },
    "Aptitude > Time & Work > Statement Question": {
        "subject": "Aptitude",
        "topic": "Time & Work",
        "subtopic": "Statement Question"
    },
    "Aptitude > Time & Work > Passage based Question": {
        "subject": "Aptitude",
        "topic": "Time & Work",
        "subtopic": "Passage based Question"
    },
    "Aptitude > Time & Work > Double filler question": {
        "subject": "Aptitude",
        "topic": "Time & Work",
        "subtopic": "Double filler question"
    },
    "Aptitude > Pipes & Cistern > Statement Question": {
        "subject": "Aptitude",
        "topic": "Pipes & Cistern",
        "subtopic": "Statement Question"
    },
    "Aptitude > Pipes & Cistern > Passage based Question": {
        "subject": "Aptitude",
        "topic": "Pipes & Cistern",
        "subtopic": "Passage based Question"
    },
    "Aptitude > Pipes & Cistern > Double filler question": {
        "subject": "Aptitude",
        "topic": "Pipes & Cistern",
        "subtopic": "Double filler question"
    },
    "Aptitude > Simple Interest > Statement Question": {
        "subject": "Aptitude",
        "topic": "Simple Interest",
        "subtopic": "Statement Question"
    },
    "Aptitude > Simple Interest > Passage based Question": {
        "subject": "Aptitude",
        "topic": "Simple Interest",
        "subtopic": "Passage based Question"
    },
    "Aptitude > Simple Interest > Double filler question": {
        "subject": "Aptitude",
        "topic": "Simple Interest",
        "subtopic": "Double filler question"
    },
    "Aptitude > Compound Interest > Statement Question": {
        "subject": "Aptitude",
        "topic": "Compound Interest",
        "subtopic": "Statement Question"
    },
    "Aptitude > Compound Interest > Passage based Question": {
        "subject": "Aptitude",
        "topic": "Compound Interest",
        "subtopic": "Passage based Question"
    },
    "Aptitude > Compound Interest > Double filler question": {
        "subject": "Aptitude",
        "topic": "Compound Interest",
        "subtopic": "Double filler question"
    },
    "Aptitude > Mixtures & Alligations > Statement Question": {
        "subject": "Aptitude",
        "topic": "Mixtures & Alligations",
        "subtopic": "Statement Question"
    },
    "Aptitude > Mixtures & Alligations > Passage based Question": {
        "subject": "Aptitude",
        "topic": "Mixtures & Alligations",
        "subtopic": "Passage based Question"
    },
    "Aptitude > Mixtures & Alligations > Double filler question": {
        "subject": "Aptitude",
        "topic": "Mixtures & Alligations",
        "subtopic": "Double filler question"
    },
    "Aptitude > Permutation & Combination > Statement Question": {
        "subject": "Aptitude",
        "topic": "Permutation & Combination",
        "subtopic": "Statement Question"
    },
    "Aptitude > Permutation & Combination > Passage based Question": {
        "subject": "Aptitude",
        "topic": "Permutation & Combination",
        "subtopic": "Passage based Question"
    },
    "Aptitude > Permutation & Combination > Double filler question": {
        "subject": "Aptitude",
        "topic": "Permutation & Combination",
        "subtopic": "Double filler question"
    },
    "Aptitude > Probability > Statement Question": {
        "subject": "Aptitude",
        "topic": "Probability",
        "subtopic": "Statement Question"
    },
    "Aptitude > Probability > Passage based Question": {
        "subject": "Aptitude",
        "topic": "Probability",
        "subtopic": "Passage based Question"
    },
    "Aptitude > Probability > Double filler question": {
        "subject": "Aptitude",
        "topic": "Probability",
        "subtopic": "Double filler question"
    },
    "Aptitude > Miscellaneous > Miscellaneous": {
        "subject": "Aptitude",
        "topic": "Miscellaneous",
        "subtopic": "Miscellaneous"
    },
    "English > Reading Comprehension > Analytical passage": {
        "subject": "English",
        "topic": "Reading Comprehension",
        "subtopic": "Analytical passage"
    },
    "English > Reading Comprehension > Informative passage": {
        "subject": "English",
        "topic": "Reading Comprehension",
        "subtopic": "Informative passage"
    },
    "English > Reading Comprehension > Banking and Economy": {
        "subject": "English",
        "topic": "Reading Comprehension",
        "subtopic": "Banking and Economy"
    },
    "English > Reading Comprehension > Story-based passage": {
        "subject": "English",
        "topic": "Reading Comprehension",
        "subtopic": "Story-based passage"
    },
    "English > Reading Comprehension > Technology": {
        "subject": "English",
        "topic": "Reading Comprehension",
        "subtopic": "Technology"
    },
    "English > Reading Comprehension > Research-based": {
        "subject": "English",
        "topic": "Reading Comprehension",
        "subtopic": "Research-based"
    },
    "English > Reading Comprehension > Health and Self-improvement": {
        "subject": "English",
        "topic": "Reading Comprehension",
        "subtopic": "Health and Self-improvement"
    },
    "English > Parajumble > Basic para jumble": {
        "subject": "English",
        "topic": "Parajumble",
        "subtopic": "Basic para jumble"
    },
    "English > Parajumble > Para jumble with exclusion or inclusion": {
        "subject": "English",
        "topic": "Parajumble",
        "subtopic": "Para jumble with exclusion or inclusion"
    },
    "English > Parajumble > Para jumble with error spotting": {
        "subject": "English",
        "topic": "Parajumble",
        "subtopic": "Para jumble with error spotting"
    },
    "English > Parajumble > Para jumble with rearrangement": {
        "subject": "English",
        "topic": "Parajumble",
        "subtopic": "Para jumble with rearrangement"
    },
    "English > Parajumble > Para jumble with a blank": {
        "subject": "English",
        "topic": "Parajumble",
        "subtopic": "Para jumble with a blank"
    },
    "English > Parajumble > Para jumble with match the columns": {
        "subject": "English",
        "topic": "Parajumble",
        "subtopic": "Para jumble with match the columns"
    },
    "English > Parajumble > Para jumble with phrasal filler": {
        "subject": "English",
        "topic": "Parajumble",
        "subtopic": "Para jumble with phrasal filler"
    },
    "English > Parajumble > Para jumble with a fixed sentence": {
        "subject": "English",
        "topic": "Parajumble",
        "subtopic": "Para jumble with a fixed sentence"
    },
    "English > Sentence Rearrangement > Rearrangement with four/five parts": {
        "subject": "English",
        "topic": "Sentence Rearrangement",
        "subtopic": "Rearrangement with four/five parts"
    },
    "English > Sentence Rearrangement > Omission of irrelevant part": {
        "subject": "English",
        "topic": "Sentence Rearrangement",
        "subtopic": "Omission of irrelevant part"
    },
    "English > Match the columns > Basic pattern with two or three columns": {
        "subject": "English",
        "topic": "Match the columns",
        "subtopic": "Basic pattern with two or three columns"
    },
    "English > Match the columns > Match the column with the connector": {
        "subject": "English",
        "topic": "Match the columns",
        "subtopic": "Match the column with the connector"
    },
    "English > Match the columns > Columns with fillers or word swap": {
        "subject": "English",
        "topic": "Match the columns",
        "subtopic": "Columns with fillers or word swap"
    },
    "English > Match the columns > Columns with error spotting": {
        "subject": "English",
        "topic": "Match the columns",
        "subtopic": "Columns with error spotting"
    },
    "English > Match the columns > Match the column with column fillers": {
        "subject": "English",
        "topic": "Match the columns",
        "subtopic": "Match the column with column fillers"
    },
    "English > Statement based > Para completion": {
        "subject": "English",
        "topic": "Statement based",
        "subtopic": "Para completion"
    },
    "English > Statement based > Paragraph inference or cause": {
        "subject": "English",
        "topic": "Statement based",
        "subtopic": "Paragraph inference or cause"
    },
    "English > Statement based > odd one out from the theme": {
        "subject": "English",
        "topic": "Statement based",
        "subtopic": "odd one out from the theme"
    },
    "English > Error Spotting > Correct sentence": {
        "subject": "English",
        "topic": "Error Spotting",
        "subtopic": "Correct sentence"
    },
    "English > Error Spotting > Incorrect sentence": {
        "subject": "English",
        "topic": "Error Spotting",
        "subtopic": "Incorrect sentence"
    },
    "English > Error Spotting > Number of errors in a sentence": {
        "subject": "English",
        "topic": "Error Spotting",
        "subtopic": "Number of errors in a sentence"
    },
    "English > Error Spotting > Error parts in a sentence": {
        "subject": "English",
        "topic": "Error Spotting",
        "subtopic": "Error parts in a sentence"
    },
    "English > Error Spotting > Error-free parts in a sentence": {
        "subject": "English",
        "topic": "Error Spotting",
        "subtopic": "Error-free parts in a sentence"
    },
    "English > Phrasal replacement > Phrasal verb replacement": {
        "subject": "English",
        "topic": "Phrasal replacement",
        "subtopic": "Phrasal verb replacement"
    },
    "English > Phrasal replacement > Phrase replacement": {
        "subject": "English",
        "topic": "Phrasal replacement",
        "subtopic": "Phrase replacement"
    },
    "English > Phrasal replacement > Choose the correct meaning of the highlighted phrase": {
        "subject": "English",
        "topic": "Phrasal replacement",
        "subtopic": "Choose the correct meaning of the highlighted phrase"
    },
    "English > Cloze test > Basic type": {
        "subject": "English",
        "topic": "Cloze test",
        "subtopic": "Basic type"
    },
    "English > Cloze test > Blanks followed by a synonym": {
        "subject": "English",
        "topic": "Cloze test",
        "subtopic": "Blanks followed by a synonym"
    },
    "English > Cloze test > Two or three options for a single blank": {
        "subject": "English",
        "topic": "Cloze test",
        "subtopic": "Two or three options for a single blank"
    },
    "English > Cloze test > Inappropriate option for the blank": {
        "subject": "English",
        "topic": "Cloze test",
        "subtopic": "Inappropriate option for the blank"
    },
    "English > Cloze test > Blanks to be filled by a phrase or phrasal verb": {
        "subject": "English",
        "topic": "Cloze test",
        "subtopic": "Blanks to be filled by a phrase or phrasal verb"
    },
    "English > Fill in the blanks > Single filler": {
        "subject": "English",
        "topic": "Fill in the blanks",
        "subtopic": "Single filler"
    },
    "English > Fill in the blanks > Double filler": {
        "subject": "English",
        "topic": "Fill in the blanks",
        "subtopic": "Double filler"
    },
    "English > Fill in the blanks > Triple filler": {
        "subject": "English",
        "topic": "Fill in the blanks",
        "subtopic": "Triple filler"
    },
    "English > Word Usage > Usage of words": {
        "subject": "English",
        "topic": "Word Usage",
        "subtopic": "Usage of words"
    },
    "English > Word Swap > Word swap in a sentence": {
        "subject": "English",
        "topic": "Word Swap",
        "subtopic": "Word swap in a sentence"
    },
    "English > Word Swap > Word swap in a passage": {
        "subject": "English",
        "topic": "Word Swap",
        "subtopic": "Word swap in a passage"
    },
    "English > Word Swap > Word swap with inappropriate word": {
        "subject": "English",
        "topic": "Word Swap",
        "subtopic": "Word swap with inappropriate word"
    },
    "English > Mis-spelt > Spelling error": {
        "subject": "English",
        "topic": "Mis-spelt",
        "subtopic": "Spelling error"
    },
    "English > Mis-spelt > Inappropriate words": {
        "subject": "English",
        "topic": "Mis-spelt",
        "subtopic": "Inappropriate words"
    },
    "English > Synonyms & Antonyms > Synonyms": {
        "subject": "English",
        "topic": "Synonyms & Antonyms",
        "subtopic": "Synonyms"
    },
    "English > Synonyms & Antonyms > Antonyms": {
        "subject": "English",
        "topic": "Synonyms & Antonyms",
        "subtopic": "Antonyms"
    },
    "English > Idioms > Meaning of the idioms": {
        "subject": "English",
        "topic": "Idioms",
        "subtopic": "Meaning of the idioms"
    },
    "English > Idioms > Meaning of the phrases": {
        "subject": "English",
        "topic": "Idioms",
        "subtopic": "Meaning of the phrases"
    },
    "English > Idioms > Fillers with Idioms": {
        "subject": "English",
        "topic": "Idioms",
        "subtopic": "Fillers with Idioms"
    },
    "English > Idioms > Fillers with Phrasal verbs": {
        "subject": "English",
        "topic": "Idioms",
        "subtopic": "Fillers with Phrasal verbs"
    },
    "English > Idioms > Similar usage of the Idiom": {
        "subject": "English",
        "topic": "Idioms",
        "subtopic": "Similar usage of the Idiom"
    },
    "English > Idioms > Similar usage of the phrase": {
        "subject": "English",
        "topic": "Idioms",
        "subtopic": "Similar usage of the phrase"
    },
    "English > Connectors/starters > Grammar-based": {
        "subject": "English",
        "topic": "Connectors/starters",
        "subtopic": "Grammar-based"
    },
    "English > Connectors/starters > Context-based": {
        "subject": "English",
        "topic": "Connectors/starters",
        "subtopic": "Context-based"
    },
    "Reasoning > Direction > Normal": {
        "subject": "Reasoning",
        "topic": "Direction",
        "subtopic": "Normal"
    },
    "Reasoning > Direction > Coded direction": {
        "subject": "Reasoning",
        "topic": "Direction",
        "subtopic": "Coded direction"
    },
    "Reasoning > Meaningful words > Meaningful word": {
        "subject": "Reasoning",
        "topic": "Meaningful words",
        "subtopic": "Meaningful word"
    },
}


# ===== SSC_RAILWAYS TAXONOMY =====

SSC_RAILWAYS_SUBJECTS: List[str] = [
    "Aptitude",
    "Computer Awareness",
    "English",
    "General Studies",
    "Reasoning",
    "Static GK",
]

SSC_RAILWAYS_TRIPLETS: List[str] = [
    "Reasoning > Analogy, Odd One Out > Based on Numbers",
    "Reasoning > Analogy, Odd One Out > Based on Alphabets",
    "Reasoning > Analogy, Odd One Out > Based on General Things",
    "Reasoning > Analogy, Odd One Out > Based on Figures",
    "Reasoning > Analogy, Odd One Out > Analogy based Questions",
    "Reasoning > Number series > Based on Sum and Difference",
    "Reasoning > Number series > Based on Double Difference",
    "Reasoning > Number series > Based on Multiplication and Division",
    "Reasoning > Number series > Based on Squares",
    "Reasoning > Number series > Based on Cubes",
    "Reasoning > Number series > Wrong Number",
    "Reasoning > Number series > Box and other shapes based problems",
    "Reasoning > Number series > Number Rearrangement",
    "Reasoning > Alphabet Test > Logical Order",
    "Reasoning > Alphabet Test > Alphabet series",
    "Reasoning > Alphabet Test > Alphanumeric series",
    "Reasoning > Alphabet Test > Word Formation Unscrambbling",
    "Reasoning > Alphabet Test > Dictionary",
    "Reasoning > Alphabet Test > Fillers",
    "Reasoning > Alphabet Test > Word Rearrangement",
    "Reasoning > Coding Decoding > Letter Coding",
    "Reasoning > Coding Decoding > Letter and Number Coding",
    "Reasoning > Coding Decoding > Symbol Coding and Message Coding",
    "Reasoning > Coding Decoding > Substitution Coding",
    "Reasoning > Mathematical Operation > Whether the given equations are correct",
    "Reasoning > Mathematical Operation > Coding Decoding based",
    "Reasoning > Mathematical Operation > Interchanging the Signs",
    "Reasoning > Mathematical Operation > Equation Balancing",
    "Reasoning > Seating Arrangement > Linear Arrangement",
    "Reasoning > Seating Arrangement > Double Row Arrangement",
    "Reasoning > Seating Arrangement > Circular Seating Arrangement",
    "Reasoning > Seating Arrangement > Rectangular Arrangement",
    "Reasoning > Seating Arrangement > Direction Based",
    "Reasoning > Blood Relations > SSC model questions",
    "Reasoning > Blood Relations > More than 3 person relationship",
    "Reasoning > Blood Relations > Coded Relations",
    "Reasoning > Ranking > Total Number of Person Given Data",
    "Reasoning > Ranking > Rank from Left or Right",
    "Reasoning > Ranking > Number of Persons between Two Persons & Either Sides of Persons",
    "Reasoning > Ranking > Rank of a Person after Changing",
    "Reasoning > Ranking > Ascending and Descending",
    "Reasoning > Direction Sense > Finding Direction and Distance",
    "Reasoning > Direction Sense > Distance and Direction with reference to a certain place or person",
    "Reasoning > Direction Sense > Shadow & (upside down) related problems",
    "Reasoning > Direction Sense > Angle related problems",
    "Reasoning > Syllogism > Positive conclusions",
    "Reasoning > Syllogism > Negative conclusions",
    "Reasoning > Syllogism > Either or",
    "Reasoning > Syllogism > Possibility",
    "Reasoning > Venn Diagrams > Finding Relationship",
    "Reasoning > Venn Diagrams > Finding Exact Region",
    "Reasoning > Assumption or Inference or Conclusion > One statement with Two Conclusion",
    "Reasoning > Assumption or Inference or Conclusion > More than two statements and Conclusion",
    "Reasoning > Assumption or Inference or Conclusion > Cause & Effect",
    "Reasoning > Clock > Angle based",
    "Reasoning > Clock > Based on Coincidence",
    "Reasoning > Clock > Mirror Clock",
    "Reasoning > Clock > Wrong Reading and other problems related to time",
    "Reasoning > Calendar > Time sequence( lies between )",
    "Reasoning > Calendar > Single statement",
    "Reasoning > Calendar > Reference statement",
    "Reasoning > Miscellaneous > Meaningful Order",
    "Reasoning > Mirror and Water Image > Mirror Image",
    "Reasoning > Mirror and Water Image > Water Image",
    "Reasoning > Paper Cutting and Folding > Triangular Paper Cutting",
    "Reasoning > Paper Cutting and Folding > Circular Paper Cutting",
    "Reasoning > Paper Cutting and Folding > Square & Rectangular Paper Cutting",
    "Reasoning > Paper Cutting and Folding > Transparent Sheets",
    "Reasoning > Cubes and Dices > Constructed and Deconstructed (unfolded cubes)",
    "Reasoning > Cubes and Dices > 2 figures",
    "Reasoning > Cubes and Dices > Painted Cubes",
    "Reasoning > Embedded Figures Matrix & Figure Completion > Simple Models",
    "Reasoning > Embedded Figures Matrix & Figure Completion > Figure Series",
    "Reasoning > Counting of Figures > Squares and Rectangle",
    "Reasoning > Counting of Figures > Triangle",
    "Reasoning > Counting of Figures > Combination of Triangle, Squares and Rectangle",
    "Reasoning > Counting of Figures > Other Shapes",
    "Reasoning > Data sufficiency > Triangle",
    "Reasoning > Statement and Course of action > Statement and Course of Action",
    "Aptitude > Simplification > BODMAS",
    "Aptitude > Simplification > Fractions",
    "Aptitude > Simplification > Recurring Fractions",
    "Aptitude > Simplification > Continued Fractions",
    "Aptitude > Simplification > Special Type Multiples in Fraction",
    "Aptitude > Simplification > Formula based (Algebra)",
    "Aptitude > Simplification > Multiples based on 9's",
    "Aptitude > Simplification > Miscellaneous",
    "Aptitude > Simplification > Law of Surds & Indices",
    "Aptitude > Simplification > Conjugation",
    "Aptitude > Simplification > Comparision of Surds (Root & Power)",
    "Aptitude > Simplification > Comparision of Surds (Addition & Substraction)",
    "Aptitude > Simplification > Square Root of an Irrational Number",
    "Aptitude > Simplification > Square Root & Cube Root",
    "Aptitude > Simplification > Special Root Series",
    "Aptitude > Number System > Types of Numbers",
    "Aptitude > Number System > Number of Zeros",
    "Aptitude > Number System > Divisibility Rules",
    "Aptitude > Number System > Successive Division",
    "Aptitude > Number System > Factors",
    "Aptitude > Number System > Squares",
    "Aptitude > Number System > Cubes",
    "Aptitude > Number System > Remainder Theorem",
    "Aptitude > Number System > Arithmetic Progression",
    "Aptitude > Number System > Geometric Progression",
    "Aptitude > Number System > Natural Numbers",
    "Aptitude > Number System > Unit Digit",
    "Aptitude > Number System > Last Two Digits",
    "Aptitude > HCF & LCM > HCF & LCM of Decimals And Fractions",
    "Aptitude > HCF & LCM > HCF Using Long Division Method",
    "Aptitude > HCF & LCM > HCF & LCM of Powers",
    "Aptitude > HCF & LCM > HCF (Basic, Same Remainder)",
    "Aptitude > HCF & LCM > HCF (Different Remainder , Same Remainder)",
    "Aptitude > HCF & LCM > LCM Basics",
    "Aptitude > HCF & LCM > LCM (Same Remainder , Different Remainder)",
    "Aptitude > HCF & LCM > LCM (Greatest (Or) Least 'n' Digit Number)",
    "Aptitude > HCF & LCM > LCM (Exactly Divisible By Another Number)",
    "Aptitude > HCF & LCM > Relation Between HCF & LCM",
    "Aptitude > HCF & LCM > Number Of Pairs",
    "Aptitude > HCF & LCM > Application Sums (HCF)",
    "Aptitude > HCF & LCM > Application Sums (LCM)",
    "Aptitude > Average > Average (Basic) Simple & Weighted",
    "Aptitude > Average > Finding Average of Given Series",
    "Aptitude > Average > Change in Average (Added To All Numbers)",
    "Aptitude > Average > Finding the Missing Number / Repeated Number",
    "Aptitude > Average > Without Replacement",
    "Aptitude > Average > With Replacement",
    "Aptitude > Average > Error on Marks (Corrected Average)",
    "Aptitude > Average > Cricket (Basics)",
    "Aptitude > Average > Batting & Bowling",
    "Aptitude > Average > Average Expenditure",
    "Aptitude > Average > Miscellaneous",
    "Aptitude > Ratio - Proportion > Compound Ratio",
    "Aptitude > Ratio - Proportion > Proportion Properties",
    "Aptitude > Ratio - Proportion > Third , Fourth & Mean Proportion",
    "Aptitude > Ratio - Proportion > Addition / Substraction Number to Make a Proportion",
    "Aptitude > Ratio - Proportion > Based on Coins",
    "Aptitude > Ratio - Proportion > Mixture Based Questions",
    "Aptitude > Ratio - Proportion > In Ratio Left/Add Some Student",
    "Aptitude > Ratio - Proportion > Income, Expenditure & Saving",
    "Aptitude > Ratio - Proportion > Based on Percentage (I = E + S)",
    "Aptitude > Ratio - Proportion > Based on Previous Year & Current Year",
    "Aptitude > Ratio - Proportion > Based on  A=BXC , B=A/C, C=A/B",
    "Aptitude > Ratio - Proportion > Based on Direct & Inversely Proportional",
    "Aptitude > Ratio - Proportion > Based on Fractions",
    "Aptitude > Ratio - Proportion > Ages",
    "Aptitude > Ratio - Proportion > Partnership - Basics",
    "Aptitude > Ratio - Proportion > Capital of Partners Are Invested For a Different Period of Time",
    "Aptitude > Ratio - Proportion > Working on Sleeping Partners",
    "Aptitude > Ratio - Proportion > Miscellaneous - Based on Previous Sums",
    "Aptitude > Mixtures & Alligation > Alligation",
    "Aptitude > Mixtures & Alligation > Based on Mixture Selling at Profit",
    "Aptitude > Mixtures & Alligation > Based on Average Concept",
    "Aptitude > Mixtures & Alligation > Based on Three Variables (Alligations)",
    "Aptitude > Mixtures & Alligation > Based on Profit Percentage & Time , Speed & Distance",
    "Aptitude > Mixtures & Alligation > Based on Amount=Value x Number of Persons",
    "Aptitude > Mixtures & Alligation > Questions Related to Other Topics Percentage, Simple Interest, Zoo (Animal Based Questions) & Income , Expenditure & Savings",
    "Aptitude > Mixtures & Alligation > Add or Removal of Some Quantity",
    "Aptitude > Mixtures & Alligation > Remove Mixture & Add Same or Different Quantities of Either of the Solutions",
    "Aptitude > Mixtures & Alligation > Alligations based Mixtures Questions",
    "Aptitude > Mixtures & Alligation > Repeated Process of Removal & Addition",
    "Aptitude > Mixtures & Alligation > Find Ratio of Repeated Process Are Given",
    "Aptitude > Mixtures & Alligation > Mixture of two things - Same quantity",
    "Aptitude > Mixtures & Alligation > Mixture of two things - Different quantities",
    "Aptitude > Percentage > Percentage to Fraction",
    "Aptitude > Percentage > Basic Problems",
    "Aptitude > Percentage > Comparing 2 Values",
    "Aptitude > Percentage > Price & Consumption",
    "Aptitude > Percentage > Price,Consumption & Quantity",
    "Aptitude > Percentage > Comparison of Numbers",
    "Aptitude > Percentage > Net Percent Change",
    "Aptitude > Percentage > Examination",
    "Aptitude > Percentage > Income, Expenditure & Savings",
    "Aptitude > Percentage > Price & Population & Depreciation",
    "Aptitude > Percentage > Election",
    "Aptitude > Percentage > Venn Diagram",
    "Aptitude > Percentage > Questions on Remaining Values",
    "Aptitude > Percentage > Fresh / Dry Fruit",
    "Aptitude > Percentage > Income tax & Error %",
    "Aptitude > Profit & Loss > Profit on Selling Price",
    "Aptitude > Profit & Loss > Profit/Loss on Number of Articles",
    "Aptitude > Profit & Loss > Variation in Selling Price",
    "Aptitude > Profit & Loss > Variation in Cost Price & Selling Price",
    "Aptitude > Profit & Loss > Same Cost Price (or) Selling price",
    "Aptitude > Profit & Loss > Total Cost Price of Two Articles",
    "Aptitude > Profit & Loss > Partial Selling",
    "Aptitude > Profit & Loss > Rotation among Different Sellers",
    "Aptitude > Profit & Loss > Ratio between Profit & Loss",
    "Aptitude > Profit & Loss > Successive Discount",
    "Aptitude > Profit & Loss > Cost Price Marked Price & Selling Price",
    "Aptitude > Profit & Loss > Dishonest Seller",
    "Aptitude > Profit & Loss > Profit by Alligation",
    "Aptitude > Profit & Loss > Miscellaneous Questions",
    "Aptitude > Simple Interest > Basic Question",
    "Aptitude > Simple Interest > Finding Principal, Rate & Time",
    "Aptitude > Simple Interest > Change in Rate and Time",
    "Aptitude > Simple Interest > Based on Ratio",
    "Aptitude > Simple Interest > Based on Distribution",
    "Aptitude > Simple Interest > Based on Alligation",
    "Aptitude > Simple Interest > Installment",
    "Aptitude > Simple Interest > Miscellaneous",
    "Aptitude > Compound Interest > Basic Questions",
    "Aptitude > Compound Interest > Half - Yearly Basis",
    "Aptitude > Compound Interest > Quarterly Basis",
    "Aptitude > Compound Interest > Half - yearly / Quarterly Basis",
    "Aptitude > Compound Interest > Different amounts at the same rate",
    "Aptitude > Compound Interest > ‘n’ times of principal",
    "Aptitude > Compound Interest > Mixed of SI and CI",
    "Aptitude > Compound Interest > Difference between SI and CI",
    "Aptitude > Compound Interest > Installment",
    "Aptitude > Compound Interest > Miscellaneous",
    "Aptitude > Time & Work > Alternate Days",
    "Aptitude > Time & Work > Wages",
    "Aptitude > Time & Work > Remaining Work or Partial Work",
    "Aptitude > Time & Work > Efficiency",
    "Aptitude > Time & Work > Chain Rule",
    "Aptitude > Time & Work > Miscellaneous",
    "Aptitude > Time & Work > Pipes and Cisterns",
    "Aptitude > Time & Distance > Usual Speed & Time",
    "Aptitude > Time & Distance > Average Speed",
    "Aptitude > Time & Distance > Ratio",
    "Aptitude > Time & Distance > Relative Speed",
    "Aptitude > Time & Distance > Change in Speed",
    "Aptitude > Time & Distance > Miscellaneous",
    "Aptitude > Time & Distance > Race",
    "Aptitude > Train > Basic Concepts",
    "Aptitude > Train > Train Theory",
    "Aptitude > Train > Relative Speed Question",
    "Aptitude > Train > Speed Ratios",
    "Aptitude > Train > Problems on Directions",
    "Aptitude > Boats & Streams > Boats & Streams",
    "Aptitude > Boats & Streams > Equation based problems",
    "Aptitude > Boats & Streams > Downstream as much as Upstream Equation based problems",
    "Aptitude > Data Interpretation > Pie-chart",
    "Aptitude > Data Interpretation > Line Graph",
    "Aptitude > Data Interpretation > Simple Bar",
    "Aptitude > Data Interpretation > Horizontal and Divide Bar",
    "Aptitude > Data Interpretation > Multi Bar",
    "Aptitude > Data Interpretation > Histogram",
    "Aptitude > Data Interpretation > Table Chart",
    "Aptitude > Data Interpretation > Miscellaneous",
    "Aptitude > Algebra > Polynomials",
    "Aptitude > Algebra > Linear equation in 2 variables",
    "Aptitude > Algebra > Solubility of Linear Equation",
    "Aptitude > Algebra > Linear Equation in 3 Variables",
    "Aptitude > Algebra > Roots of Quadratic Equation",
    "Aptitude > Algebra > Problems on Roots of Quadratic Equation",
    "Aptitude > Algebra > Max & Min of Quadratic expression",
    "Aptitude > Algebra > Maximum & Minimum Value",
    "Aptitude > Algebra > Roots of Cubic Equation",
    "Aptitude > Algebra > Factors & Remainders",
    "Aptitude > Algebra > Algebraic Identities",
    "Aptitude > Algebra > Squares",
    "Aptitude > Algebra > Cube",
    "Aptitude > Algebra > Square Root & Cube Root",
    "Aptitude > Algebra > Special Formula Part",
    "Aptitude > Algebra > Sum of squares = 0",
    "Aptitude > Algebra > Inverse Functions",
    "Aptitude > Algebra > Reverse order",
    "Aptitude > Algebra > Special Stats",
    "Aptitude > Algebra > Symmetric equation",
    "Aptitude > Algebra > Value Putting",
    "Aptitude > Algebra > Square Root of Irrational Numbers",
    "Aptitude > Algebra > Componendo - Dividendo",
    "Aptitude > Geometry > Types of Angles",
    "Aptitude > Geometry > Lines & Angles Concepts",
    "Aptitude > Geometry > Triangles-Properties of a Triangle",
    "Aptitude > Geometry > Triangles-Exterior Angle Property",
    "Aptitude > Geometry > Triangles-Basic Question",
    "Aptitude > Geometry > Condition for formation of a Triangle",
    "Aptitude > Geometry > Sine Rule",
    "Aptitude > Geometry > Triangles-Stewart’s Theorem",
    "Aptitude > Geometry > Triangles-Internal bisector",
    "Aptitude > Geometry > Types of Triangle",
    "Aptitude > Geometry > Isosceles Triangle",
    "Aptitude > Geometry > Equilateral Triangle",
    "Aptitude > Geometry > Triangles-On the basis of Angles",
    "Aptitude > Geometry > Congruent Triangle",
    "Aptitude > Geometry > Triangles-Similarity",
    "Aptitude > Geometry > Similarity of Right Angle Triangle",
    "Aptitude > Geometry > Basic Proportionality Theorem",
    "Aptitude > Geometry > Centers of Triangle",
    "Aptitude > Geometry > Median Property",
    "Aptitude > Geometry > Apollonius's Theorem",
    "Aptitude > Geometry > Median in a Right-Angled Triangle",
    "Aptitude > Geometry > Incentre",
    "Aptitude > Geometry > Inradius",
    "Aptitude > Geometry > Ex-Circle",
    "Aptitude > Geometry > Circumcenter",
    "Aptitude > Geometry > Circumcentre in Triangles",
    "Aptitude > Geometry > Circumcentre in Right Angle Triangle",
    "Aptitude > Geometry > Orthocentre",
    "Aptitude > Geometry > Orthocentre - Height and Side Ratio",
    "Aptitude > Geometry > Orthocenter - Altitude in Terms of the Sides",
    "Aptitude > Geometry > Interior Angle Bisector Theorem",
    "Aptitude > Geometry > Length of Angle Bisector",
    "Aptitude > Geometry > Mass Point Geometry",
    "Aptitude > Geometry > Circle - Chord",
    "Aptitude > Geometry > Circles - Property",
    "Aptitude > Geometry > Circles - Basic question",
    "Aptitude > Geometry > Circles - Two chords",
    "Aptitude > Geometry > Circles - Secants intersect",
    "Aptitude > Geometry > Circles - Secants & Tangent",
    "Aptitude > Geometry > Circles - Length of the Chord",
    "Aptitude > Geometry > Circles - Two Parallel Chords",
    "Aptitude > Geometry > Circles - Tangent",
    "Aptitude > Geometry > Circles - Alternate Segment Theorem",
    "Aptitude > Geometry > Circles - Circumscribing a circle",
    "Aptitude > Geometry > Circle -Touch Externally",
    "Aptitude > Geometry > Circle - Intersect each other",
    "Aptitude > Geometry > Circle - Intersecting Circles",
    "Aptitude > Geometry > Circle - Concentric Circles",
    "Aptitude > Geometry > Circle - Touch Externally",
    "Aptitude > Geometry > Circle - three circle with radii",
    "Aptitude > Geometry > Direct Common Tangent",
    "Aptitude > Geometry > Transverse Common Tangent",
    "Aptitude > Geometry > Circle- two circle intersecting internally",
    "Aptitude > Geometry > Cyclic Quadrilateral",
    "Aptitude > Geometry > Area of Cyclic Quadrilateral",
    "Aptitude > Geometry > Quadrilateral",
    "Aptitude > Geometry > Quadrilateral-Types",
    "Aptitude > Geometry > Parallelogram",
    "Aptitude > Geometry > Rectangle",
    "Aptitude > Geometry > Square",
    "Aptitude > Geometry > Rhombus",
    "Aptitude > Geometry > Trapezium",
    "Aptitude > Geometry > Polygon",
    "Aptitude > Geometry > Angles of polygon",
    "Aptitude > Geometry > Area of Regular Polygon",
    "Aptitude > Geometry > Hexagon",
    "Aptitude > Geometry > Hexagon-Equal Divisions of Area",
    "Aptitude > Geometry > Hexagon-Basic Question",
    "Aptitude > Geometry > Octagon",
    "Aptitude > Coordinate Geometry > Distance between Two Points",
    "Aptitude > Coordinate Geometry > Section of a Line",
    "Aptitude > Coordinate Geometry > Slope of a Line",
    "Aptitude > Coordinate Geometry > Angle between Two Lines",
    "Aptitude > Coordinate Geometry > Equation of lines",
    "Aptitude > Coordinate Geometry > Distance of a Point from a Line",
    "Aptitude > Coordinate Geometry > Distance between Parallel Lines",
    "Aptitude > Coordinate Geometry > Reflection of a Point",
    "Aptitude > Mensuration > Polygons",
    "Aptitude > Mensuration > Triangles",
    "Aptitude > Mensuration > Classification of Triangles",
    "Aptitude > Mensuration > Area and Perimeter of Triangle",
    "Aptitude > Mensuration > Area of cyclic Quadrilateral",
    "Aptitude > Mensuration > Square",
    "Aptitude > Mensuration > Rectangle",
    "Aptitude > Mensuration > Rhombus",
    "Aptitude > Mensuration > Parallelogram",
    "Aptitude > Mensuration > Trapezium",
    "Aptitude > Mensuration > Hexagon",
    "Aptitude > Mensuration > Octagon",
    "Aptitude > Mensuration > Circle",
    "Aptitude > Mensuration > Ratio of Radius, Perimeter & Area of Circle",
    "Aptitude > Mensuration > Circular Ring",
    "Aptitude > Mensuration > Area and Perimeter of Semi Circle & Quarter Circle",
    "Aptitude > Mensuration > Sector of a Circle",
    "Aptitude > Mensuration > Square and Circle",
    "Aptitude > Mensuration > Triangles & Circles",
    "Aptitude > Mensuration > Square, Rectangle & Triangle",
    "Aptitude > Mensuration > Same perimeter",
    "Aptitude > Mensuration > Rectangle path",
    "Aptitude > Mensuration > Cost based on Area & Perimeter",
    "Aptitude > Mensuration > Band Around Circles",
    "Aptitude > Mensuration > Prism",
    "Aptitude > Mensuration > Cube",
    "Aptitude > Mensuration > Cuboid",
    "Aptitude > Mensuration > Right Circular Cylinder",
    "Aptitude > Mensuration > Pyramid",
    "Aptitude > Mensuration > Cone",
    "Aptitude > Mensuration > Frustom of a Cone",
    "Aptitude > Mensuration > Ratio of Volume of Pyramid",
    "Aptitude > Mensuration > Sphere",
    "Aptitude > Mensuration > Hollow Sphere",
    "Aptitude > Mensuration > Hemisphere",
    "Aptitude > Mensuration > Relation between Volumes of Cylinder, Cone and Hemisphere",
    "Aptitude > Mensuration > Conversion of Solids from One Form to Another",
    "Aptitude > Mensuration > Area or Volume after Removal of Solids",
    "Aptitude > Mensuration > Volume of Water Flowing from a Pipe",
    "Aptitude > Mensuration > Useful Results",
    "Aptitude > Mensuration > One Figure inside Another",
    "Aptitude > Mensuration > Figure Based Questions",
    "Aptitude > Trigonometry > Trigonometry circular measure of angles",
    "Aptitude > Trigonometry > Circular system",
    "Aptitude > Trigonometry > Basic Identities of Trigonometry",
    "Aptitude > Trigonometry > Trigonometric Ratios of some specific angles",
    "Aptitude > Trigonometry > Quadrant System",
    "Aptitude > Trigonometry > Sum of two angles (𝛼+𝛽)=90",
    "Aptitude > Trigonometry > Basic Identities",
    "Aptitude > Trigonometry > Based on Putting Value",
    "Aptitude > Trigonometry > x+1/x=2",
    "Aptitude > Trigonometry > Basic Identity (compound angles)",
    "Aptitude > Trigonometry > Maximum & minimum value of trigonometrix",
    "Aptitude > Height & Distance > Height & Distance - Basic concept",
    "Aptitude > Height & Distance > Based on Angle Changed:",
    "Aptitude > Height & Distance > Height & Distance - Complementary Angle",
    "Aptitude > Probability > Probability",
    "Aptitude > Statistics > Class intervals , Frequency",
    "Aptitude > Statistics > Mean,Mode,Median",
    "English > Noun > Noun",
    "English > Noun > Types of Nouns",
    "English > Noun > Countable and Uncountable",
    "English > Noun > Rules Based on Numbers",
    "English > Noun > Based on Gender",
    "English > Noun > Based On Noun - Case",
    "English > Noun > Confusing Words",
    "English > Noun > Find the Correct One",
    "English > Pronoun > Pronoun",
    "English > Pronoun > Rules Based on Possessive Pronoun",
    "English > Pronoun > Relative Pronoun",
    "English > Pronoun > Reciprocal Pronoun",
    "English > Pronoun > Pronoun Workout",
    "English > Verb > Forms of Verb",
    "English > Verb > Regular Verbs",
    "English > Verb > Modal verbs",
    "English > Verb > Rules Based on Verbs",
    "English > Adverb > Adverb",
    "English > Adverb > Adverb of Place",
    "English > Adverb > Rules for Adverb",
    "English > Adverb > workouts",
    "English > Tenses > Tenses",
    "English > Adjectives > Distributive Adjectives",
    "English > Adjectives > Rules - Degrees of Comparison",
    "English > Prepositions > Prepositions",
    "English > Subject Verb Agreement > Rule 1-5",
    "English > Subject Verb Agreement > Rule 06-12",
    "English > Subject Verb Agreement > Rule 13-19",
    "English > Subject Verb Agreement > Rule 20-24",
    "English > Subject Verb Agreement > Rule 25-28",
    "English > Subject Verb Agreement > Sentence Improvement & Error Spotting",
    "English > Articles > Articles-Use of a/an",
    "English > Articles > Articles-Use of The",
    "English > Articles > Omission",
    "English > Articles > exercise",
    "English > Conjunction > Co-ordinating Conjunctions",
    "English > Conjunction > Subordinating Conjunction",
    "English > Conjunction > Subordinating conjunctions & Correlative conjunctions",
    "English > Conjunction > Rules",
    "English > Speech > Sentence types",
    "English > Speech > Change of Persons",
    "English > Speech > Change of Time",
    "English > Speech > Change of Time-Type 2",
    "English > Speech > Other Parts of Speech and Assertive Sentence",
    "English > Speech > Interrogative Sentence",
    "English > Speech > Imperative Sentence",
    "English > Speech > Optative and Exclamatory Sentences",
    "English > Speech > Previous year Question",
    "English > Speech > Revision",
    "English > Voice > 5 Rules",
    "English > Voice > Passive Formation of the Types of Tenses",
    "English > Voice > Continous tense",
    "English > Voice > Perfect tense",
    "English > Voice > Modal auxillary verb",
    "English > Voice > Imperative",
    "English > Voice > Interrogative",
    "English > Voice > Prepositions",
    "English > Voice > Miscellaneous",
    "English > Voice > Exercise",
    "English > Reading Comprehension > Questions",
    "English > Cloze Test > Cloze Test",
    "English > Synonyms & Antonyms > Synonyms",
    "English > Synonyms & Antonyms > Antonyms",
    "English > One Word Substitution > One Word Substitution",
    "English > Idioms & Phrases > Basics",
    "English > Idioms & Phrases > Idiom-based on weather",
    "English > Idioms & Phrases > Idiom-based on colour",
    "English > Idioms & Phrases > Idiom-based on body parts",
    "English > Idioms & Phrases > Idiom-based on numbers",
    "English > Idioms & Phrases > Phrasal Verbs",
    "English > Question Tag > Rules 1-5",
    "English > Question Tag > Rules 6-11",
    "English > Question Tag > Exercise",
    "English > Conditional Clauses > Zero and first",
    "English > Conditional Clauses > Second & three Conditional",
    "English > Conditional Clauses > Mixed and Unless",
    "English > Conditional Clauses > Spot the Error",
    "General Studies > Ancient - History > Prehistoric And Indus Valley",
    "General Studies > Ancient - History > Vedic Age",
    "General Studies > Ancient - History > Jainism",
    "General Studies > Ancient - History > Buddhism",
    "General Studies > Ancient - History > Mahajanapadas",
    "General Studies > Ancient - History > Mauryan Dynasty",
    "General Studies > Ancient - History > Gupta Dynasty",
    "General Studies > Ancient - History > Vardhana Dynasty",
    "General Studies > Ancient - History > sangam",
    "General Studies > Ancient - History > Chola Dynasty",
    "General Studies > Ancient - History > Pallavas",
    "General Studies > Ancient - History > Saka Era",
    "General Studies > Ancient - History > Kushanas",
    "General Studies > Medieval - History > Foreign Invasions",
    "General Studies > Medieval - History > Delhi Sultanate",
    "General Studies > Medieval - History > Slave Dynasty",
    "General Studies > Medieval - History > Khilji Dynasty",
    "General Studies > Medieval - History > Tughlaq Dynasty",
    "General Studies > Medieval - History > Sayyid Dynasty",
    "General Studies > Medieval - History > Lodi Dynasty",
    "General Studies > Medieval - History > Mughal Period",
    "General Studies > Medieval - History > Babur",
    "General Studies > Medieval - History > Humayun and Sher Shah Suri",
    "General Studies > Medieval - History > Akbar",
    "General Studies > Medieval - History > Jahangir",
    "General Studies > Medieval - History > Shah Jahan",
    "General Studies > Medieval - History > Aurangzeb",
    "General Studies > Medieval - History > Sufism",
    "General Studies > Medieval - History > Sikh Guru",
    "General Studies > Medieval - History > Maratha Empire",
    "General Studies > Medieval - History > Vijaynagar Empire",
    "General Studies > Medieval - History > Wars and Treaties",
    "General Studies > Medieval - History > Miscellaneous",
    "General Studies > Modern - History > The Revolt of 1857",
    "General Studies > Modern - History > Governors and Viceroys",
    "General Studies > Modern - History > British acts and Policies",
    "General Studies > Modern - History > Partition of Bengal and Swadeshi Movements",
    "General Studies > Modern - History > Gandhian Era",
    "General Studies > Modern - History > Expansion of British Rule",
    "General Studies > Modern - History > The Revolutionaries",
    "General Studies > Modern - History > Struggle for Independence",
    "General Studies > Modern - History > Socio Religious Reforms",
    "General Studies > Modern - History > Indian National Congress and Its Sessions",
    "General Studies > Modern - History > Muslim league",
    "General Studies > Modern - History > Leaders",
    "General Studies > Modern - History > Miscellaneous",
    "General Studies > Geography > Solar system and its planets",
    "General Studies > Geography > Longitudes and latitudes",
    "General Studies > Geography > Continents and Oceans",
    "General Studies > Geography > Neighbouring Countries of India",
    "General Studies > Geography > Indian Drainage System",
    "General Studies > Geography > World Drainage System",
    "General Studies > Geography > Minerals and Energy Resources in India",
    "General Studies > Geography > Agriculture",
    "General Studies > Geography > Soil",
    "General Studies > Geography > Crops",
    "General Studies > Geography > Vegetation",
    "General Studies > Geography > Climate",
    "General Studies > Geography > Industries",
    "General Studies > Geography > NAP/WLS/Biosphere Reserves/Various Initiatives",
    "General Studies > Geography > Physiographic Division of India",
    "General Studies > Geography > Transportation",
    "General Studies > Geography > Population",
    "General Studies > Geography > Atmosphere",
    "General Studies > Geography > Rocks",
    "General Studies > Geography > Mountain",
    "General Studies > Geography > Volcano",
    "General Studies > Geography > World geography and Map",
    "General Studies > Geography > Environment",
    "General Studies > Polity > Constitution",
    "General Studies > Polity > Sources of Indian Constitution",
    "General Studies > Polity > Articles, Schedules, Parts and list",
    "General Studies > Polity > Amendments",
    "General Studies > Polity > DPSP",
    "General Studies > Polity > Fundamental Rights and Duties",
    "General Studies > Polity > Committee Reports",
    "General Studies > Polity > Parliament",
    "General Studies > Polity > President, Vice President and Prime Minister",
    "General Studies > Polity > Judiciary",
    "General Studies > Polity > Government Bodies",
    "General Studies > Polity > Polity of neighbouring countries",
    "General Studies > Polity > Important Cases",
    "General Studies > Economy > Basics of Economy",
    "General Studies > Economy > Concepts of Demand and Supply",
    "General Studies > Economy > Cost, Production, Consumption and Market",
    "General Studies > Economy > National Income, Inflation, Budget,Taxation and GDP",
    "General Studies > Economy > Money Banking and Financial Institutions",
    "General Studies > Economy > Navratna / Maharatna / PSUs",
    "General Studies > Economy > International Organisations",
    "General Studies > Economy > Government Schemes",
    "General Studies > Economy > Five - Year Plans",
    "General Studies > Economy > LPG",
    "General Studies > Economy > Indian Economy : Central Problems and Planning",
    "General Studies > Economy > Stock, Debentures and Foreign trade",
    "General Studies > Economy > Fiscal Policy and Monetary Policy",
    "General Studies > Economy > Miscellaneous",
    "General Studies > Physics > Light and Optics",
    "General Studies > Physics > Heat and Thermodynamics",
    "General Studies > Physics > Fluid Mechanics",
    "General Studies > Physics > Electric Current and Its Effects",
    "General Studies > Physics > Laws",
    "General Studies > Physics > Force and Pressure",
    "General Studies > Physics > Sound",
    "General Studies > Physics > Gravitation",
    "General Studies > Physics > Work and Energy",
    "General Studies > Physics > Wave",
    "General Studies > Physics > Radioactivity",
    "General Studies > Physics > Discoveries",
    "General Studies > Physics > Units and Measurements",
    "General Studies > Physics > Miscellaneous",
    "General Studies > Chemistry > Structure of Atom",
    "General Studies > Chemistry > Compounds",
    "General Studies > Chemistry > Metals, Non-metals and Alloys",
    "General Studies > Chemistry > Acid, Bases and Salt",
    "General Studies > Chemistry > Metallurgy",
    "General Studies > Chemistry > Organic Chemistry",
    "General Studies > Chemistry > Periodic table",
    "General Studies > Chemistry > Ideal Gas Law",
    "General Studies > Chemistry > Chemical Properties",
    "General Studies > Chemistry > Solutions",
    "General Studies > Chemistry > Chemistry in Everyday life",
    "General Studies > Chemistry > Discoveries",
    "General Studies > Chemistry > Common Names",
    "General Studies > Chemistry > Miscellaneous",
    "General Studies > Biology > Scientific Names",
    "General Studies > Biology > Nutrition in Animals",
    "General Studies > Biology > Nutrition in plants",
    "General Studies > Biology > Deficiency and Diseases",
    "General Studies > Biology > Reproduction in Animals",
    "General Studies > Biology > Reproduction in Plants",
    "General Studies > Biology > Cell: Basic Unit of life",
    "General Studies > Biology > Sensory Organs",
    "General Studies > Biology > Circulatory System",
    "General Studies > Biology > Excretory System",
    "General Studies > Biology > Endocrine/Exocrine system",
    "General Studies > Biology > Respiratory system",
    "General Studies > Biology > Digestive system",
    "General Studies > Biology > Nervous system",
    "General Studies > Biology > Skeleton system",
    "General Studies > Biology > Plant Kingdom",
    "General Studies > Biology > Animal Kingdom",
    "General Studies > Biology > Micro organisms",
    "General Studies > Biology > Enzymes and Hormones",
    "General Studies > Biology > Discoveries and vaccines",
    "General Studies > Biology > Scientific Study",
    "General Studies > Biology > Miscellaneous",
    "Static GK > Static GK > Important Days",
    "Static GK > Static GK > Appointments",
    "Static GK > Static GK > Places",
    "Static GK > Static GK > Arts Personality",
    "Static GK > Static GK > Head Quaters",
    "Static GK > Static GK > Arts Awards",
    "Static GK > Static GK > Musical Instruments",
    "Static GK > Static GK > Festivals",
    "Static GK > Static GK > Dances",
    "Static GK > Static GK > Fairs",
    "Static GK > Static GK > Songs",
    "Static GK > Static GK > Painting/Dress/Tribes",
    "Static GK > Static GK > First in India/World",
    "Static GK > Static GK > Sports",
    "Static GK > Static GK > Books and Authors",
    "Static GK > Static GK > Famous Personalities",
    "Static GK > Static GK > States G.K.",
    "Static GK > Static GK > Organisations",
    "Static GK > Static GK > World G.K",
    "Static GK > Static GK > Full forms",
    "Static GK > Static GK > Religious Places",
    "Static GK > Static GK > Awards",
    "Static GK > Static GK > Important Events",
    "Static GK > Static GK > Founders",
    "Static GK > Static GK > Schemes",
    "Static GK > Static GK > Discoveries",
    "Static GK > Static GK > IUCN Red Lisst",
    "Static GK > Static GK > Themes",
    "Static GK > Static GK > Miscellaneous",
    "Computer Awareness > Computer Basics > Organization of a computer",
    "Computer Awareness > Computer Basics > Central Processing Unit (CPU)",
    "Computer Awareness > Computer Basics > Input/Output devices",
    "Computer Awareness > Computer Basics > Computer memory",
    "Computer Awareness > Computer Basics > Memory organization",
    "Computer Awareness > Computer Basics > Backup devices",
    "Computer Awareness > Computer Basics > PORTs",
    "Computer Awareness > Computer Basics > Windows Explorer",
    "Computer Awareness > Computer Basics > Keyboard shortcuts",
    "Computer Awareness > Software > Windows Operating System",
    "Computer Awareness > Software > Basics of Microsoft Office (MS Word, MS Excel, PowerPoint)",
    "Computer Awareness > Working with Internet and E-mails > Web Browsing & Searching",
    "Computer Awareness > Working with Internet and E-mails > Downloading & Uploading",
    "Computer Awareness > Working with Internet and E-mails > Managing an E-mail Account",
    "Computer Awareness > Working with Internet and E-mails > e-Banking",
    "Computer Awareness > Networking and Cyber Security > Networking devices and protocols",
    "Computer Awareness > Networking and Cyber Security > Network and information security threats (hacking, virus, worms, Trojan, etc.)",
    "Computer Awareness > Networking and Cyber Security > Preventive measures",
]

SSC_RAILWAYS_TRIPLET_DICT: Dict[str, Dict[str, str]] = {
    "Reasoning > Analogy, Odd One Out > Based on Numbers": {
        "subject": "Reasoning",
        "topic": "Analogy, Odd One Out",
        "subtopic": "Based on Numbers"
    },
    "Reasoning > Analogy, Odd One Out > Based on Alphabets": {
        "subject": "Reasoning",
        "topic": "Analogy, Odd One Out",
        "subtopic": "Based on Alphabets"
    },
    "Reasoning > Analogy, Odd One Out > Based on General Things": {
        "subject": "Reasoning",
        "topic": "Analogy, Odd One Out",
        "subtopic": "Based on General Things"
    },
    "Reasoning > Analogy, Odd One Out > Based on Figures": {
        "subject": "Reasoning",
        "topic": "Analogy, Odd One Out",
        "subtopic": "Based on Figures"
    },
    "Reasoning > Analogy, Odd One Out > Analogy based Questions": {
        "subject": "Reasoning",
        "topic": "Analogy, Odd One Out",
        "subtopic": "Analogy based Questions"
    },
    "Reasoning > Number series > Based on Sum and Difference": {
        "subject": "Reasoning",
        "topic": "Number series",
        "subtopic": "Based on Sum and Difference"
    },
    "Reasoning > Number series > Based on Double Difference": {
        "subject": "Reasoning",
        "topic": "Number series",
        "subtopic": "Based on Double Difference"
    },
    "Reasoning > Number series > Based on Multiplication and Division": {
        "subject": "Reasoning",
        "topic": "Number series",
        "subtopic": "Based on Multiplication and Division"
    },
    "Reasoning > Number series > Based on Squares": {
        "subject": "Reasoning",
        "topic": "Number series",
        "subtopic": "Based on Squares"
    },
    "Reasoning > Number series > Based on Cubes": {
        "subject": "Reasoning",
        "topic": "Number series",
        "subtopic": "Based on Cubes"
    },
    "Reasoning > Number series > Wrong Number": {
        "subject": "Reasoning",
        "topic": "Number series",
        "subtopic": "Wrong Number"
    },
    "Reasoning > Number series > Box and other shapes based problems": {
        "subject": "Reasoning",
        "topic": "Number series",
        "subtopic": "Box and other shapes based problems"
    },
    "Reasoning > Number series > Number Rearrangement": {
        "subject": "Reasoning",
        "topic": "Number series",
        "subtopic": "Number Rearrangement"
    },
    "Reasoning > Alphabet Test > Logical Order": {
        "subject": "Reasoning",
        "topic": "Alphabet Test",
        "subtopic": "Logical Order"
    },
    "Reasoning > Alphabet Test > Alphabet series": {
        "subject": "Reasoning",
        "topic": "Alphabet Test",
        "subtopic": "Alphabet series"
    },
    "Reasoning > Alphabet Test > Alphanumeric series": {
        "subject": "Reasoning",
        "topic": "Alphabet Test",
        "subtopic": "Alphanumeric series"
    },
    "Reasoning > Alphabet Test > Word Formation Unscrambbling": {
        "subject": "Reasoning",
        "topic": "Alphabet Test",
        "subtopic": "Word Formation Unscrambbling"
    },
    "Reasoning > Alphabet Test > Dictionary": {
        "subject": "Reasoning",
        "topic": "Alphabet Test",
        "subtopic": "Dictionary"
    },
    "Reasoning > Alphabet Test > Fillers": {
        "subject": "Reasoning",
        "topic": "Alphabet Test",
        "subtopic": "Fillers"
    },
    "Reasoning > Alphabet Test > Word Rearrangement": {
        "subject": "Reasoning",
        "topic": "Alphabet Test",
        "subtopic": "Word Rearrangement"
    },
    "Reasoning > Coding Decoding > Letter Coding": {
        "subject": "Reasoning",
        "topic": "Coding Decoding",
        "subtopic": "Letter Coding"
    },
    "Reasoning > Coding Decoding > Letter and Number Coding": {
        "subject": "Reasoning",
        "topic": "Coding Decoding",
        "subtopic": "Letter and Number Coding"
    },
    "Reasoning > Coding Decoding > Symbol Coding and Message Coding": {
        "subject": "Reasoning",
        "topic": "Coding Decoding",
        "subtopic": "Symbol Coding and Message Coding"
    },
    "Reasoning > Coding Decoding > Substitution Coding": {
        "subject": "Reasoning",
        "topic": "Coding Decoding",
        "subtopic": "Substitution Coding"
    },
    "Reasoning > Mathematical Operation > Whether the given equations are correct": {
        "subject": "Reasoning",
        "topic": "Mathematical Operation",
        "subtopic": "Whether the given equations are correct"
    },
    "Reasoning > Mathematical Operation > Coding Decoding based": {
        "subject": "Reasoning",
        "topic": "Mathematical Operation",
        "subtopic": "Coding Decoding based"
    },
    "Reasoning > Mathematical Operation > Interchanging the Signs": {
        "subject": "Reasoning",
        "topic": "Mathematical Operation",
        "subtopic": "Interchanging the Signs"
    },
    "Reasoning > Mathematical Operation > Equation Balancing": {
        "subject": "Reasoning",
        "topic": "Mathematical Operation",
        "subtopic": "Equation Balancing"
    },
    "Reasoning > Seating Arrangement > Linear Arrangement": {
        "subject": "Reasoning",
        "topic": "Seating Arrangement",
        "subtopic": "Linear Arrangement"
    },
    "Reasoning > Seating Arrangement > Double Row Arrangement": {
        "subject": "Reasoning",
        "topic": "Seating Arrangement",
        "subtopic": "Double Row Arrangement"
    },
    "Reasoning > Seating Arrangement > Circular Seating Arrangement": {
        "subject": "Reasoning",
        "topic": "Seating Arrangement",
        "subtopic": "Circular Seating Arrangement"
    },
    "Reasoning > Seating Arrangement > Rectangular Arrangement": {
        "subject": "Reasoning",
        "topic": "Seating Arrangement",
        "subtopic": "Rectangular Arrangement"
    },
    "Reasoning > Seating Arrangement > Direction Based": {
        "subject": "Reasoning",
        "topic": "Seating Arrangement",
        "subtopic": "Direction Based"
    },
    "Reasoning > Blood Relations > SSC model questions": {
        "subject": "Reasoning",
        "topic": "Blood Relations",
        "subtopic": "SSC model questions"
    },
    "Reasoning > Blood Relations > More than 3 person relationship": {
        "subject": "Reasoning",
        "topic": "Blood Relations",
        "subtopic": "More than 3 person relationship"
    },
    "Reasoning > Blood Relations > Coded Relations": {
        "subject": "Reasoning",
        "topic": "Blood Relations",
        "subtopic": "Coded Relations"
    },
    "Reasoning > Ranking > Total Number of Person Given Data": {
        "subject": "Reasoning",
        "topic": "Ranking",
        "subtopic": "Total Number of Person Given Data"
    },
    "Reasoning > Ranking > Rank from Left or Right": {
        "subject": "Reasoning",
        "topic": "Ranking",
        "subtopic": "Rank from Left or Right"
    },
    "Reasoning > Ranking > Number of Persons between Two Persons & Either Sides of Persons": {
        "subject": "Reasoning",
        "topic": "Ranking",
        "subtopic": "Number of Persons between Two Persons & Either Sides of Persons"
    },
    "Reasoning > Ranking > Rank of a Person after Changing": {
        "subject": "Reasoning",
        "topic": "Ranking",
        "subtopic": "Rank of a Person after Changing"
    },
    "Reasoning > Ranking > Ascending and Descending": {
        "subject": "Reasoning",
        "topic": "Ranking",
        "subtopic": "Ascending and Descending"
    },
    "Reasoning > Direction Sense > Finding Direction and Distance": {
        "subject": "Reasoning",
        "topic": "Direction Sense",
        "subtopic": "Finding Direction and Distance"
    },
    "Reasoning > Direction Sense > Distance and Direction with reference to a certain place or person": {
        "subject": "Reasoning",
        "topic": "Direction Sense",
        "subtopic": "Distance and Direction with reference to a certain place or person"
    },
    "Reasoning > Direction Sense > Shadow & (upside down) related problems": {
        "subject": "Reasoning",
        "topic": "Direction Sense",
        "subtopic": "Shadow & (upside down) related problems"
    },
    "Reasoning > Direction Sense > Angle related problems": {
        "subject": "Reasoning",
        "topic": "Direction Sense",
        "subtopic": "Angle related problems"
    },
    "Reasoning > Syllogism > Positive conclusions": {
        "subject": "Reasoning",
        "topic": "Syllogism",
        "subtopic": "Positive conclusions"
    },
    "Reasoning > Syllogism > Negative conclusions": {
        "subject": "Reasoning",
        "topic": "Syllogism",
        "subtopic": "Negative conclusions"
    },
    "Reasoning > Syllogism > Either or": {
        "subject": "Reasoning",
        "topic": "Syllogism",
        "subtopic": "Either or"
    },
    "Reasoning > Syllogism > Possibility": {
        "subject": "Reasoning",
        "topic": "Syllogism",
        "subtopic": "Possibility"
    },
    "Reasoning > Venn Diagrams > Finding Relationship": {
        "subject": "Reasoning",
        "topic": "Venn Diagrams",
        "subtopic": "Finding Relationship"
    },
    "Reasoning > Venn Diagrams > Finding Exact Region": {
        "subject": "Reasoning",
        "topic": "Venn Diagrams",
        "subtopic": "Finding Exact Region"
    },
    "Reasoning > Assumption or Inference or Conclusion > One statement with Two Conclusion": {
        "subject": "Reasoning",
        "topic": "Assumption or Inference or Conclusion",
        "subtopic": "One statement with Two Conclusion"
    },
    "Reasoning > Assumption or Inference or Conclusion > More than two statements and Conclusion": {
        "subject": "Reasoning",
        "topic": "Assumption or Inference or Conclusion",
        "subtopic": "More than two statements and Conclusion"
    },
    "Reasoning > Assumption or Inference or Conclusion > Cause & Effect": {
        "subject": "Reasoning",
        "topic": "Assumption or Inference or Conclusion",
        "subtopic": "Cause & Effect"
    },
    "Reasoning > Clock > Angle based": {
        "subject": "Reasoning",
        "topic": "Clock",
        "subtopic": "Angle based"
    },
    "Reasoning > Clock > Based on Coincidence": {
        "subject": "Reasoning",
        "topic": "Clock",
        "subtopic": "Based on Coincidence"
    },
    "Reasoning > Clock > Mirror Clock": {
        "subject": "Reasoning",
        "topic": "Clock",
        "subtopic": "Mirror Clock"
    },
    "Reasoning > Clock > Wrong Reading and other problems related to time": {
        "subject": "Reasoning",
        "topic": "Clock",
        "subtopic": "Wrong Reading and other problems related to time"
    },
    "Reasoning > Calendar > Time sequence( lies between )": {
        "subject": "Reasoning",
        "topic": "Calendar",
        "subtopic": "Time sequence( lies between )"
    },
    "Reasoning > Calendar > Single statement": {
        "subject": "Reasoning",
        "topic": "Calendar",
        "subtopic": "Single statement"
    },
    "Reasoning > Calendar > Reference statement": {
        "subject": "Reasoning",
        "topic": "Calendar",
        "subtopic": "Reference statement"
    },
    "Reasoning > Miscellaneous > Meaningful Order": {
        "subject": "Reasoning",
        "topic": "Miscellaneous",
        "subtopic": "Meaningful Order"
    },
    "Reasoning > Mirror and Water Image > Mirror Image": {
        "subject": "Reasoning",
        "topic": "Mirror and Water Image",
        "subtopic": "Mirror Image"
    },
    "Reasoning > Mirror and Water Image > Water Image": {
        "subject": "Reasoning",
        "topic": "Mirror and Water Image",
        "subtopic": "Water Image"
    },
    "Reasoning > Paper Cutting and Folding > Triangular Paper Cutting": {
        "subject": "Reasoning",
        "topic": "Paper Cutting and Folding",
        "subtopic": "Triangular Paper Cutting"
    },
    "Reasoning > Paper Cutting and Folding > Circular Paper Cutting": {
        "subject": "Reasoning",
        "topic": "Paper Cutting and Folding",
        "subtopic": "Circular Paper Cutting"
    },
    "Reasoning > Paper Cutting and Folding > Square & Rectangular Paper Cutting": {
        "subject": "Reasoning",
        "topic": "Paper Cutting and Folding",
        "subtopic": "Square & Rectangular Paper Cutting"
    },
    "Reasoning > Paper Cutting and Folding > Transparent Sheets": {
        "subject": "Reasoning",
        "topic": "Paper Cutting and Folding",
        "subtopic": "Transparent Sheets"
    },
    "Reasoning > Cubes and Dices > Constructed and Deconstructed (unfolded cubes)": {
        "subject": "Reasoning",
        "topic": "Cubes and Dices",
        "subtopic": "Constructed and Deconstructed (unfolded cubes)"
    },
    "Reasoning > Cubes and Dices > 2 figures": {
        "subject": "Reasoning",
        "topic": "Cubes and Dices",
        "subtopic": "2 figures"
    },
    "Reasoning > Cubes and Dices > Painted Cubes": {
        "subject": "Reasoning",
        "topic": "Cubes and Dices",
        "subtopic": "Painted Cubes"
    },
    "Reasoning > Embedded Figures Matrix & Figure Completion > Simple Models": {
        "subject": "Reasoning",
        "topic": "Embedded Figures Matrix & Figure Completion",
        "subtopic": "Simple Models"
    },
    "Reasoning > Embedded Figures Matrix & Figure Completion > Figure Series": {
        "subject": "Reasoning",
        "topic": "Embedded Figures Matrix & Figure Completion",
        "subtopic": "Figure Series"
    },
    "Reasoning > Counting of Figures > Squares and Rectangle": {
        "subject": "Reasoning",
        "topic": "Counting of Figures",
        "subtopic": "Squares and Rectangle"
    },
    "Reasoning > Counting of Figures > Triangle": {
        "subject": "Reasoning",
        "topic": "Counting of Figures",
        "subtopic": "Triangle"
    },
    "Reasoning > Counting of Figures > Combination of Triangle, Squares and Rectangle": {
        "subject": "Reasoning",
        "topic": "Counting of Figures",
        "subtopic": "Combination of Triangle, Squares and Rectangle"
    },
    "Reasoning > Counting of Figures > Other Shapes": {
        "subject": "Reasoning",
        "topic": "Counting of Figures",
        "subtopic": "Other Shapes"
    },
    "Reasoning > Data sufficiency > Triangle": {
        "subject": "Reasoning",
        "topic": "Data sufficiency",
        "subtopic": "Triangle"
    },
    "Reasoning > Statement and Course of action > Statement and Course of Action": {
        "subject": "Reasoning",
        "topic": "Statement and Course of action",
        "subtopic": "Statement and Course of Action"
    },
    "Aptitude > Simplification > BODMAS": {
        "subject": "Aptitude",
        "topic": "Simplification",
        "subtopic": "BODMAS"
    },
    "Aptitude > Simplification > Fractions": {
        "subject": "Aptitude",
        "topic": "Simplification",
        "subtopic": "Fractions"
    },
    "Aptitude > Simplification > Recurring Fractions": {
        "subject": "Aptitude",
        "topic": "Simplification",
        "subtopic": "Recurring Fractions"
    },
    "Aptitude > Simplification > Continued Fractions": {
        "subject": "Aptitude",
        "topic": "Simplification",
        "subtopic": "Continued Fractions"
    },
    "Aptitude > Simplification > Special Type Multiples in Fraction": {
        "subject": "Aptitude",
        "topic": "Simplification",
        "subtopic": "Special Type Multiples in Fraction"
    },
    "Aptitude > Simplification > Formula based (Algebra)": {
        "subject": "Aptitude",
        "topic": "Simplification",
        "subtopic": "Formula based (Algebra)"
    },
    "Aptitude > Simplification > Multiples based on 9's": {
        "subject": "Aptitude",
        "topic": "Simplification",
        "subtopic": "Multiples based on 9's"
    },
    "Aptitude > Simplification > Miscellaneous": {
        "subject": "Aptitude",
        "topic": "Simplification",
        "subtopic": "Miscellaneous"
    },
    "Aptitude > Simplification > Law of Surds & Indices": {
        "subject": "Aptitude",
        "topic": "Simplification",
        "subtopic": "Law of Surds & Indices"
    },
    "Aptitude > Simplification > Conjugation": {
        "subject": "Aptitude",
        "topic": "Simplification",
        "subtopic": "Conjugation"
    },
    "Aptitude > Simplification > Comparision of Surds (Root & Power)": {
        "subject": "Aptitude",
        "topic": "Simplification",
        "subtopic": "Comparision of Surds (Root & Power)"
    },
    "Aptitude > Simplification > Comparision of Surds (Addition & Substraction)": {
        "subject": "Aptitude",
        "topic": "Simplification",
        "subtopic": "Comparision of Surds (Addition & Substraction)"
    },
    "Aptitude > Simplification > Square Root of an Irrational Number": {
        "subject": "Aptitude",
        "topic": "Simplification",
        "subtopic": "Square Root of an Irrational Number"
    },
    "Aptitude > Simplification > Square Root & Cube Root": {
        "subject": "Aptitude",
        "topic": "Simplification",
        "subtopic": "Square Root & Cube Root"
    },
    "Aptitude > Simplification > Special Root Series": {
        "subject": "Aptitude",
        "topic": "Simplification",
        "subtopic": "Special Root Series"
    },
    "Aptitude > Number System > Types of Numbers": {
        "subject": "Aptitude",
        "topic": "Number System",
        "subtopic": "Types of Numbers"
    },
    "Aptitude > Number System > Number of Zeros": {
        "subject": "Aptitude",
        "topic": "Number System",
        "subtopic": "Number of Zeros"
    },
    "Aptitude > Number System > Divisibility Rules": {
        "subject": "Aptitude",
        "topic": "Number System",
        "subtopic": "Divisibility Rules"
    },
    "Aptitude > Number System > Successive Division": {
        "subject": "Aptitude",
        "topic": "Number System",
        "subtopic": "Successive Division"
    },
    "Aptitude > Number System > Factors": {
        "subject": "Aptitude",
        "topic": "Number System",
        "subtopic": "Factors"
    },
    "Aptitude > Number System > Squares": {
        "subject": "Aptitude",
        "topic": "Number System",
        "subtopic": "Squares"
    },
    "Aptitude > Number System > Cubes": {
        "subject": "Aptitude",
        "topic": "Number System",
        "subtopic": "Cubes"
    },
    "Aptitude > Number System > Remainder Theorem": {
        "subject": "Aptitude",
        "topic": "Number System",
        "subtopic": "Remainder Theorem"
    },
    "Aptitude > Number System > Arithmetic Progression": {
        "subject": "Aptitude",
        "topic": "Number System",
        "subtopic": "Arithmetic Progression"
    },
    "Aptitude > Number System > Geometric Progression": {
        "subject": "Aptitude",
        "topic": "Number System",
        "subtopic": "Geometric Progression"
    },
    "Aptitude > Number System > Natural Numbers": {
        "subject": "Aptitude",
        "topic": "Number System",
        "subtopic": "Natural Numbers"
    },
    "Aptitude > Number System > Unit Digit": {
        "subject": "Aptitude",
        "topic": "Number System",
        "subtopic": "Unit Digit"
    },
    "Aptitude > Number System > Last Two Digits": {
        "subject": "Aptitude",
        "topic": "Number System",
        "subtopic": "Last Two Digits"
    },
    "Aptitude > HCF & LCM > HCF & LCM of Decimals And Fractions": {
        "subject": "Aptitude",
        "topic": "HCF & LCM",
        "subtopic": "HCF & LCM of Decimals And Fractions"
    },
    "Aptitude > HCF & LCM > HCF Using Long Division Method": {
        "subject": "Aptitude",
        "topic": "HCF & LCM",
        "subtopic": "HCF Using Long Division Method"
    },
    "Aptitude > HCF & LCM > HCF & LCM of Powers": {
        "subject": "Aptitude",
        "topic": "HCF & LCM",
        "subtopic": "HCF & LCM of Powers"
    },
    "Aptitude > HCF & LCM > HCF (Basic, Same Remainder)": {
        "subject": "Aptitude",
        "topic": "HCF & LCM",
        "subtopic": "HCF (Basic, Same Remainder)"
    },
    "Aptitude > HCF & LCM > HCF (Different Remainder , Same Remainder)": {
        "subject": "Aptitude",
        "topic": "HCF & LCM",
        "subtopic": "HCF (Different Remainder , Same Remainder)"
    },
    "Aptitude > HCF & LCM > LCM Basics": {
        "subject": "Aptitude",
        "topic": "HCF & LCM",
        "subtopic": "LCM Basics"
    },
    "Aptitude > HCF & LCM > LCM (Same Remainder , Different Remainder)": {
        "subject": "Aptitude",
        "topic": "HCF & LCM",
        "subtopic": "LCM (Same Remainder , Different Remainder)"
    },
    "Aptitude > HCF & LCM > LCM (Greatest (Or) Least 'n' Digit Number)": {
        "subject": "Aptitude",
        "topic": "HCF & LCM",
        "subtopic": "LCM (Greatest (Or) Least 'n' Digit Number)"
    },
    "Aptitude > HCF & LCM > LCM (Exactly Divisible By Another Number)": {
        "subject": "Aptitude",
        "topic": "HCF & LCM",
        "subtopic": "LCM (Exactly Divisible By Another Number)"
    },
    "Aptitude > HCF & LCM > Relation Between HCF & LCM": {
        "subject": "Aptitude",
        "topic": "HCF & LCM",
        "subtopic": "Relation Between HCF & LCM"
    },
    "Aptitude > HCF & LCM > Number Of Pairs": {
        "subject": "Aptitude",
        "topic": "HCF & LCM",
        "subtopic": "Number Of Pairs"
    },
    "Aptitude > HCF & LCM > Application Sums (HCF)": {
        "subject": "Aptitude",
        "topic": "HCF & LCM",
        "subtopic": "Application Sums (HCF)"
    },
    "Aptitude > HCF & LCM > Application Sums (LCM)": {
        "subject": "Aptitude",
        "topic": "HCF & LCM",
        "subtopic": "Application Sums (LCM)"
    },
    "Aptitude > Average > Average (Basic) Simple & Weighted": {
        "subject": "Aptitude",
        "topic": "Average",
        "subtopic": "Average (Basic) Simple & Weighted"
    },
    "Aptitude > Average > Finding Average of Given Series": {
        "subject": "Aptitude",
        "topic": "Average",
        "subtopic": "Finding Average of Given Series"
    },
    "Aptitude > Average > Change in Average (Added To All Numbers)": {
        "subject": "Aptitude",
        "topic": "Average",
        "subtopic": "Change in Average (Added To All Numbers)"
    },
    "Aptitude > Average > Finding the Missing Number / Repeated Number": {
        "subject": "Aptitude",
        "topic": "Average",
        "subtopic": "Finding the Missing Number / Repeated Number"
    },
    "Aptitude > Average > Without Replacement": {
        "subject": "Aptitude",
        "topic": "Average",
        "subtopic": "Without Replacement"
    },
    "Aptitude > Average > With Replacement": {
        "subject": "Aptitude",
        "topic": "Average",
        "subtopic": "With Replacement"
    },
    "Aptitude > Average > Error on Marks (Corrected Average)": {
        "subject": "Aptitude",
        "topic": "Average",
        "subtopic": "Error on Marks (Corrected Average)"
    },
    "Aptitude > Average > Cricket (Basics)": {
        "subject": "Aptitude",
        "topic": "Average",
        "subtopic": "Cricket (Basics)"
    },
    "Aptitude > Average > Batting & Bowling": {
        "subject": "Aptitude",
        "topic": "Average",
        "subtopic": "Batting & Bowling"
    },
    "Aptitude > Average > Average Expenditure": {
        "subject": "Aptitude",
        "topic": "Average",
        "subtopic": "Average Expenditure"
    },
    "Aptitude > Average > Miscellaneous": {
        "subject": "Aptitude",
        "topic": "Average",
        "subtopic": "Miscellaneous"
    },
    "Aptitude > Ratio - Proportion > Compound Ratio": {
        "subject": "Aptitude",
        "topic": "Ratio - Proportion",
        "subtopic": "Compound Ratio"
    },
    "Aptitude > Ratio - Proportion > Proportion Properties": {
        "subject": "Aptitude",
        "topic": "Ratio - Proportion",
        "subtopic": "Proportion Properties"
    },
    "Aptitude > Ratio - Proportion > Third , Fourth & Mean Proportion": {
        "subject": "Aptitude",
        "topic": "Ratio - Proportion",
        "subtopic": "Third , Fourth & Mean Proportion"
    },
    "Aptitude > Ratio - Proportion > Addition / Substraction Number to Make a Proportion": {
        "subject": "Aptitude",
        "topic": "Ratio - Proportion",
        "subtopic": "Addition / Substraction Number to Make a Proportion"
    },
    "Aptitude > Ratio - Proportion > Based on Coins": {
        "subject": "Aptitude",
        "topic": "Ratio - Proportion",
        "subtopic": "Based on Coins"
    },
    "Aptitude > Ratio - Proportion > Mixture Based Questions": {
        "subject": "Aptitude",
        "topic": "Ratio - Proportion",
        "subtopic": "Mixture Based Questions"
    },
    "Aptitude > Ratio - Proportion > In Ratio Left/Add Some Student": {
        "subject": "Aptitude",
        "topic": "Ratio - Proportion",
        "subtopic": "In Ratio Left/Add Some Student"
    },
    "Aptitude > Ratio - Proportion > Income, Expenditure & Saving": {
        "subject": "Aptitude",
        "topic": "Ratio - Proportion",
        "subtopic": "Income, Expenditure & Saving"
    },
    "Aptitude > Ratio - Proportion > Based on Percentage (I = E + S)": {
        "subject": "Aptitude",
        "topic": "Ratio - Proportion",
        "subtopic": "Based on Percentage (I = E + S)"
    },
    "Aptitude > Ratio - Proportion > Based on Previous Year & Current Year": {
        "subject": "Aptitude",
        "topic": "Ratio - Proportion",
        "subtopic": "Based on Previous Year & Current Year"
    },
    "Aptitude > Ratio - Proportion > Based on  A=BXC , B=A/C, C=A/B": {
        "subject": "Aptitude",
        "topic": "Ratio - Proportion",
        "subtopic": "Based on  A=BXC , B=A/C, C=A/B"
    },
    "Aptitude > Ratio - Proportion > Based on Direct & Inversely Proportional": {
        "subject": "Aptitude",
        "topic": "Ratio - Proportion",
        "subtopic": "Based on Direct & Inversely Proportional"
    },
    "Aptitude > Ratio - Proportion > Based on Fractions": {
        "subject": "Aptitude",
        "topic": "Ratio - Proportion",
        "subtopic": "Based on Fractions"
    },
    "Aptitude > Ratio - Proportion > Ages": {
        "subject": "Aptitude",
        "topic": "Ratio - Proportion",
        "subtopic": "Ages"
    },
    "Aptitude > Ratio - Proportion > Partnership - Basics": {
        "subject": "Aptitude",
        "topic": "Ratio - Proportion",
        "subtopic": "Partnership - Basics"
    },
    "Aptitude > Ratio - Proportion > Capital of Partners Are Invested For a Different Period of Time": {
        "subject": "Aptitude",
        "topic": "Ratio - Proportion",
        "subtopic": "Capital of Partners Are Invested For a Different Period of Time"
    },
    "Aptitude > Ratio - Proportion > Working on Sleeping Partners": {
        "subject": "Aptitude",
        "topic": "Ratio - Proportion",
        "subtopic": "Working on Sleeping Partners"
    },
    "Aptitude > Ratio - Proportion > Miscellaneous - Based on Previous Sums": {
        "subject": "Aptitude",
        "topic": "Ratio - Proportion",
        "subtopic": "Miscellaneous - Based on Previous Sums"
    },
    "Aptitude > Mixtures & Alligation > Alligation": {
        "subject": "Aptitude",
        "topic": "Mixtures & Alligation",
        "subtopic": "Alligation"
    },
    "Aptitude > Mixtures & Alligation > Based on Mixture Selling at Profit": {
        "subject": "Aptitude",
        "topic": "Mixtures & Alligation",
        "subtopic": "Based on Mixture Selling at Profit"
    },
    "Aptitude > Mixtures & Alligation > Based on Average Concept": {
        "subject": "Aptitude",
        "topic": "Mixtures & Alligation",
        "subtopic": "Based on Average Concept"
    },
    "Aptitude > Mixtures & Alligation > Based on Three Variables (Alligations)": {
        "subject": "Aptitude",
        "topic": "Mixtures & Alligation",
        "subtopic": "Based on Three Variables (Alligations)"
    },
    "Aptitude > Mixtures & Alligation > Based on Profit Percentage & Time , Speed & Distance": {
        "subject": "Aptitude",
        "topic": "Mixtures & Alligation",
        "subtopic": "Based on Profit Percentage & Time , Speed & Distance"
    },
    "Aptitude > Mixtures & Alligation > Based on Amount=Value x Number of Persons": {
        "subject": "Aptitude",
        "topic": "Mixtures & Alligation",
        "subtopic": "Based on Amount=Value x Number of Persons"
    },
    "Aptitude > Mixtures & Alligation > Questions Related to Other Topics Percentage, Simple Interest, Zoo (Animal Based Questions) & Income , Expenditure & Savings": {
        "subject": "Aptitude",
        "topic": "Mixtures & Alligation",
        "subtopic": "Questions Related to Other Topics Percentage, Simple Interest, Zoo (Animal Based Questions) & Income , Expenditure & Savings"
    },
    "Aptitude > Mixtures & Alligation > Add or Removal of Some Quantity": {
        "subject": "Aptitude",
        "topic": "Mixtures & Alligation",
        "subtopic": "Add or Removal of Some Quantity"
    },
    "Aptitude > Mixtures & Alligation > Remove Mixture & Add Same or Different Quantities of Either of the Solutions": {
        "subject": "Aptitude",
        "topic": "Mixtures & Alligation",
        "subtopic": "Remove Mixture & Add Same or Different Quantities of Either of the Solutions"
    },
    "Aptitude > Mixtures & Alligation > Alligations based Mixtures Questions": {
        "subject": "Aptitude",
        "topic": "Mixtures & Alligation",
        "subtopic": "Alligations based Mixtures Questions"
    },
    "Aptitude > Mixtures & Alligation > Repeated Process of Removal & Addition": {
        "subject": "Aptitude",
        "topic": "Mixtures & Alligation",
        "subtopic": "Repeated Process of Removal & Addition"
    },
    "Aptitude > Mixtures & Alligation > Find Ratio of Repeated Process Are Given": {
        "subject": "Aptitude",
        "topic": "Mixtures & Alligation",
        "subtopic": "Find Ratio of Repeated Process Are Given"
    },
    "Aptitude > Mixtures & Alligation > Mixture of two things - Same quantity": {
        "subject": "Aptitude",
        "topic": "Mixtures & Alligation",
        "subtopic": "Mixture of two things - Same quantity"
    },
    "Aptitude > Mixtures & Alligation > Mixture of two things - Different quantities": {
        "subject": "Aptitude",
        "topic": "Mixtures & Alligation",
        "subtopic": "Mixture of two things - Different quantities"
    },
    "Aptitude > Percentage > Percentage to Fraction": {
        "subject": "Aptitude",
        "topic": "Percentage",
        "subtopic": "Percentage to Fraction"
    },
    "Aptitude > Percentage > Basic Problems": {
        "subject": "Aptitude",
        "topic": "Percentage",
        "subtopic": "Basic Problems"
    },
    "Aptitude > Percentage > Comparing 2 Values": {
        "subject": "Aptitude",
        "topic": "Percentage",
        "subtopic": "Comparing 2 Values"
    },
    "Aptitude > Percentage > Price & Consumption": {
        "subject": "Aptitude",
        "topic": "Percentage",
        "subtopic": "Price & Consumption"
    },
    "Aptitude > Percentage > Price,Consumption & Quantity": {
        "subject": "Aptitude",
        "topic": "Percentage",
        "subtopic": "Price,Consumption & Quantity"
    },
    "Aptitude > Percentage > Comparison of Numbers": {
        "subject": "Aptitude",
        "topic": "Percentage",
        "subtopic": "Comparison of Numbers"
    },
    "Aptitude > Percentage > Net Percent Change": {
        "subject": "Aptitude",
        "topic": "Percentage",
        "subtopic": "Net Percent Change"
    },
    "Aptitude > Percentage > Examination": {
        "subject": "Aptitude",
        "topic": "Percentage",
        "subtopic": "Examination"
    },
    "Aptitude > Percentage > Income, Expenditure & Savings": {
        "subject": "Aptitude",
        "topic": "Percentage",
        "subtopic": "Income, Expenditure & Savings"
    },
    "Aptitude > Percentage > Price & Population & Depreciation": {
        "subject": "Aptitude",
        "topic": "Percentage",
        "subtopic": "Price & Population & Depreciation"
    },
    "Aptitude > Percentage > Election": {
        "subject": "Aptitude",
        "topic": "Percentage",
        "subtopic": "Election"
    },
    "Aptitude > Percentage > Venn Diagram": {
        "subject": "Aptitude",
        "topic": "Percentage",
        "subtopic": "Venn Diagram"
    },
    "Aptitude > Percentage > Questions on Remaining Values": {
        "subject": "Aptitude",
        "topic": "Percentage",
        "subtopic": "Questions on Remaining Values"
    },
    "Aptitude > Percentage > Fresh / Dry Fruit": {
        "subject": "Aptitude",
        "topic": "Percentage",
        "subtopic": "Fresh / Dry Fruit"
    },
    "Aptitude > Percentage > Income tax & Error %": {
        "subject": "Aptitude",
        "topic": "Percentage",
        "subtopic": "Income tax & Error %"
    },
    "Aptitude > Profit & Loss > Profit on Selling Price": {
        "subject": "Aptitude",
        "topic": "Profit & Loss",
        "subtopic": "Profit on Selling Price"
    },
    "Aptitude > Profit & Loss > Profit/Loss on Number of Articles": {
        "subject": "Aptitude",
        "topic": "Profit & Loss",
        "subtopic": "Profit/Loss on Number of Articles"
    },
    "Aptitude > Profit & Loss > Variation in Selling Price": {
        "subject": "Aptitude",
        "topic": "Profit & Loss",
        "subtopic": "Variation in Selling Price"
    },
    "Aptitude > Profit & Loss > Variation in Cost Price & Selling Price": {
        "subject": "Aptitude",
        "topic": "Profit & Loss",
        "subtopic": "Variation in Cost Price & Selling Price"
    },
    "Aptitude > Profit & Loss > Same Cost Price (or) Selling price": {
        "subject": "Aptitude",
        "topic": "Profit & Loss",
        "subtopic": "Same Cost Price (or) Selling price"
    },
    "Aptitude > Profit & Loss > Total Cost Price of Two Articles": {
        "subject": "Aptitude",
        "topic": "Profit & Loss",
        "subtopic": "Total Cost Price of Two Articles"
    },
    "Aptitude > Profit & Loss > Partial Selling": {
        "subject": "Aptitude",
        "topic": "Profit & Loss",
        "subtopic": "Partial Selling"
    },
    "Aptitude > Profit & Loss > Rotation among Different Sellers": {
        "subject": "Aptitude",
        "topic": "Profit & Loss",
        "subtopic": "Rotation among Different Sellers"
    },
    "Aptitude > Profit & Loss > Ratio between Profit & Loss": {
        "subject": "Aptitude",
        "topic": "Profit & Loss",
        "subtopic": "Ratio between Profit & Loss"
    },
    "Aptitude > Profit & Loss > Successive Discount": {
        "subject": "Aptitude",
        "topic": "Profit & Loss",
        "subtopic": "Successive Discount"
    },
    "Aptitude > Profit & Loss > Cost Price Marked Price & Selling Price": {
        "subject": "Aptitude",
        "topic": "Profit & Loss",
        "subtopic": "Cost Price Marked Price & Selling Price"
    },
    "Aptitude > Profit & Loss > Dishonest Seller": {
        "subject": "Aptitude",
        "topic": "Profit & Loss",
        "subtopic": "Dishonest Seller"
    },
    "Aptitude > Profit & Loss > Profit by Alligation": {
        "subject": "Aptitude",
        "topic": "Profit & Loss",
        "subtopic": "Profit by Alligation"
    },
    "Aptitude > Profit & Loss > Miscellaneous Questions": {
        "subject": "Aptitude",
        "topic": "Profit & Loss",
        "subtopic": "Miscellaneous Questions"
    },
    "Aptitude > Simple Interest > Basic Question": {
        "subject": "Aptitude",
        "topic": "Simple Interest",
        "subtopic": "Basic Question"
    },
    "Aptitude > Simple Interest > Finding Principal, Rate & Time": {
        "subject": "Aptitude",
        "topic": "Simple Interest",
        "subtopic": "Finding Principal, Rate & Time"
    },
    "Aptitude > Simple Interest > Change in Rate and Time": {
        "subject": "Aptitude",
        "topic": "Simple Interest",
        "subtopic": "Change in Rate and Time"
    },
    "Aptitude > Simple Interest > Based on Ratio": {
        "subject": "Aptitude",
        "topic": "Simple Interest",
        "subtopic": "Based on Ratio"
    },
    "Aptitude > Simple Interest > Based on Distribution": {
        "subject": "Aptitude",
        "topic": "Simple Interest",
        "subtopic": "Based on Distribution"
    },
    "Aptitude > Simple Interest > Based on Alligation": {
        "subject": "Aptitude",
        "topic": "Simple Interest",
        "subtopic": "Based on Alligation"
    },
    "Aptitude > Simple Interest > Installment": {
        "subject": "Aptitude",
        "topic": "Simple Interest",
        "subtopic": "Installment"
    },
    "Aptitude > Simple Interest > Miscellaneous": {
        "subject": "Aptitude",
        "topic": "Simple Interest",
        "subtopic": "Miscellaneous"
    },
    "Aptitude > Compound Interest > Basic Questions": {
        "subject": "Aptitude",
        "topic": "Compound Interest",
        "subtopic": "Basic Questions"
    },
    "Aptitude > Compound Interest > Half - Yearly Basis": {
        "subject": "Aptitude",
        "topic": "Compound Interest",
        "subtopic": "Half - Yearly Basis"
    },
    "Aptitude > Compound Interest > Quarterly Basis": {
        "subject": "Aptitude",
        "topic": "Compound Interest",
        "subtopic": "Quarterly Basis"
    },
    "Aptitude > Compound Interest > Half - yearly / Quarterly Basis": {
        "subject": "Aptitude",
        "topic": "Compound Interest",
        "subtopic": "Half - yearly / Quarterly Basis"
    },
    "Aptitude > Compound Interest > Different amounts at the same rate": {
        "subject": "Aptitude",
        "topic": "Compound Interest",
        "subtopic": "Different amounts at the same rate"
    },
    "Aptitude > Compound Interest > ‘n’ times of principal": {
        "subject": "Aptitude",
        "topic": "Compound Interest",
        "subtopic": "‘n’ times of principal"
    },
    "Aptitude > Compound Interest > Mixed of SI and CI": {
        "subject": "Aptitude",
        "topic": "Compound Interest",
        "subtopic": "Mixed of SI and CI"
    },
    "Aptitude > Compound Interest > Difference between SI and CI": {
        "subject": "Aptitude",
        "topic": "Compound Interest",
        "subtopic": "Difference between SI and CI"
    },
    "Aptitude > Compound Interest > Installment": {
        "subject": "Aptitude",
        "topic": "Compound Interest",
        "subtopic": "Installment"
    },
    "Aptitude > Compound Interest > Miscellaneous": {
        "subject": "Aptitude",
        "topic": "Compound Interest",
        "subtopic": "Miscellaneous"
    },
    "Aptitude > Time & Work > Alternate Days": {
        "subject": "Aptitude",
        "topic": "Time & Work",
        "subtopic": "Alternate Days"
    },
    "Aptitude > Time & Work > Wages": {
        "subject": "Aptitude",
        "topic": "Time & Work",
        "subtopic": "Wages"
    },
    "Aptitude > Time & Work > Remaining Work or Partial Work": {
        "subject": "Aptitude",
        "topic": "Time & Work",
        "subtopic": "Remaining Work or Partial Work"
    },
    "Aptitude > Time & Work > Efficiency": {
        "subject": "Aptitude",
        "topic": "Time & Work",
        "subtopic": "Efficiency"
    },
    "Aptitude > Time & Work > Chain Rule": {
        "subject": "Aptitude",
        "topic": "Time & Work",
        "subtopic": "Chain Rule"
    },
    "Aptitude > Time & Work > Miscellaneous": {
        "subject": "Aptitude",
        "topic": "Time & Work",
        "subtopic": "Miscellaneous"
    },
    "Aptitude > Time & Work > Pipes and Cisterns": {
        "subject": "Aptitude",
        "topic": "Time & Work",
        "subtopic": "Pipes and Cisterns"
    },
    "Aptitude > Time & Distance > Usual Speed & Time": {
        "subject": "Aptitude",
        "topic": "Time & Distance",
        "subtopic": "Usual Speed & Time"
    },
    "Aptitude > Time & Distance > Average Speed": {
        "subject": "Aptitude",
        "topic": "Time & Distance",
        "subtopic": "Average Speed"
    },
    "Aptitude > Time & Distance > Ratio": {
        "subject": "Aptitude",
        "topic": "Time & Distance",
        "subtopic": "Ratio"
    },
    "Aptitude > Time & Distance > Relative Speed": {
        "subject": "Aptitude",
        "topic": "Time & Distance",
        "subtopic": "Relative Speed"
    },
    "Aptitude > Time & Distance > Change in Speed": {
        "subject": "Aptitude",
        "topic": "Time & Distance",
        "subtopic": "Change in Speed"
    },
    "Aptitude > Time & Distance > Miscellaneous": {
        "subject": "Aptitude",
        "topic": "Time & Distance",
        "subtopic": "Miscellaneous"
    },
    "Aptitude > Time & Distance > Race": {
        "subject": "Aptitude",
        "topic": "Time & Distance",
        "subtopic": "Race"
    },
    "Aptitude > Train > Basic Concepts": {
        "subject": "Aptitude",
        "topic": "Train",
        "subtopic": "Basic Concepts"
    },
    "Aptitude > Train > Train Theory": {
        "subject": "Aptitude",
        "topic": "Train",
        "subtopic": "Train Theory"
    },
    "Aptitude > Train > Relative Speed Question": {
        "subject": "Aptitude",
        "topic": "Train",
        "subtopic": "Relative Speed Question"
    },
    "Aptitude > Train > Speed Ratios": {
        "subject": "Aptitude",
        "topic": "Train",
        "subtopic": "Speed Ratios"
    },
    "Aptitude > Train > Problems on Directions": {
        "subject": "Aptitude",
        "topic": "Train",
        "subtopic": "Problems on Directions"
    },
    "Aptitude > Boats & Streams > Boats & Streams": {
        "subject": "Aptitude",
        "topic": "Boats & Streams",
        "subtopic": "Boats & Streams"
    },
    "Aptitude > Boats & Streams > Equation based problems": {
        "subject": "Aptitude",
        "topic": "Boats & Streams",
        "subtopic": "Equation based problems"
    },
    "Aptitude > Boats & Streams > Downstream as much as Upstream Equation based problems": {
        "subject": "Aptitude",
        "topic": "Boats & Streams",
        "subtopic": "Downstream as much as Upstream Equation based problems"
    },
    "Aptitude > Data Interpretation > Pie-chart": {
        "subject": "Aptitude",
        "topic": "Data Interpretation",
        "subtopic": "Pie-chart"
    },
    "Aptitude > Data Interpretation > Line Graph": {
        "subject": "Aptitude",
        "topic": "Data Interpretation",
        "subtopic": "Line Graph"
    },
    "Aptitude > Data Interpretation > Simple Bar": {
        "subject": "Aptitude",
        "topic": "Data Interpretation",
        "subtopic": "Simple Bar"
    },
    "Aptitude > Data Interpretation > Horizontal and Divide Bar": {
        "subject": "Aptitude",
        "topic": "Data Interpretation",
        "subtopic": "Horizontal and Divide Bar"
    },
    "Aptitude > Data Interpretation > Multi Bar": {
        "subject": "Aptitude",
        "topic": "Data Interpretation",
        "subtopic": "Multi Bar"
    },
    "Aptitude > Data Interpretation > Histogram": {
        "subject": "Aptitude",
        "topic": "Data Interpretation",
        "subtopic": "Histogram"
    },
    "Aptitude > Data Interpretation > Table Chart": {
        "subject": "Aptitude",
        "topic": "Data Interpretation",
        "subtopic": "Table Chart"
    },
    "Aptitude > Data Interpretation > Miscellaneous": {
        "subject": "Aptitude",
        "topic": "Data Interpretation",
        "subtopic": "Miscellaneous"
    },
    "Aptitude > Algebra > Polynomials": {
        "subject": "Aptitude",
        "topic": "Algebra",
        "subtopic": "Polynomials"
    },
    "Aptitude > Algebra > Linear equation in 2 variables": {
        "subject": "Aptitude",
        "topic": "Algebra",
        "subtopic": "Linear equation in 2 variables"
    },
    "Aptitude > Algebra > Solubility of Linear Equation": {
        "subject": "Aptitude",
        "topic": "Algebra",
        "subtopic": "Solubility of Linear Equation"
    },
    "Aptitude > Algebra > Linear Equation in 3 Variables": {
        "subject": "Aptitude",
        "topic": "Algebra",
        "subtopic": "Linear Equation in 3 Variables"
    },
    "Aptitude > Algebra > Roots of Quadratic Equation": {
        "subject": "Aptitude",
        "topic": "Algebra",
        "subtopic": "Roots of Quadratic Equation"
    },
    "Aptitude > Algebra > Problems on Roots of Quadratic Equation": {
        "subject": "Aptitude",
        "topic": "Algebra",
        "subtopic": "Problems on Roots of Quadratic Equation"
    },
    "Aptitude > Algebra > Max & Min of Quadratic expression": {
        "subject": "Aptitude",
        "topic": "Algebra",
        "subtopic": "Max & Min of Quadratic expression"
    },
    "Aptitude > Algebra > Maximum & Minimum Value": {
        "subject": "Aptitude",
        "topic": "Algebra",
        "subtopic": "Maximum & Minimum Value"
    },
    "Aptitude > Algebra > Roots of Cubic Equation": {
        "subject": "Aptitude",
        "topic": "Algebra",
        "subtopic": "Roots of Cubic Equation"
    },
    "Aptitude > Algebra > Factors & Remainders": {
        "subject": "Aptitude",
        "topic": "Algebra",
        "subtopic": "Factors & Remainders"
    },
    "Aptitude > Algebra > Algebraic Identities": {
        "subject": "Aptitude",
        "topic": "Algebra",
        "subtopic": "Algebraic Identities"
    },
    "Aptitude > Algebra > Squares": {
        "subject": "Aptitude",
        "topic": "Algebra",
        "subtopic": "Squares"
    },
    "Aptitude > Algebra > Cube": {
        "subject": "Aptitude",
        "topic": "Algebra",
        "subtopic": "Cube"
    },
    "Aptitude > Algebra > Square Root & Cube Root": {
        "subject": "Aptitude",
        "topic": "Algebra",
        "subtopic": "Square Root & Cube Root"
    },
    "Aptitude > Algebra > Special Formula Part": {
        "subject": "Aptitude",
        "topic": "Algebra",
        "subtopic": "Special Formula Part"
    },
    "Aptitude > Algebra > Sum of squares = 0": {
        "subject": "Aptitude",
        "topic": "Algebra",
        "subtopic": "Sum of squares = 0"
    },
    "Aptitude > Algebra > Inverse Functions": {
        "subject": "Aptitude",
        "topic": "Algebra",
        "subtopic": "Inverse Functions"
    },
    "Aptitude > Algebra > Reverse order": {
        "subject": "Aptitude",
        "topic": "Algebra",
        "subtopic": "Reverse order"
    },
    "Aptitude > Algebra > Special Stats": {
        "subject": "Aptitude",
        "topic": "Algebra",
        "subtopic": "Special Stats"
    },
    "Aptitude > Algebra > Symmetric equation": {
        "subject": "Aptitude",
        "topic": "Algebra",
        "subtopic": "Symmetric equation"
    },
    "Aptitude > Algebra > Value Putting": {
        "subject": "Aptitude",
        "topic": "Algebra",
        "subtopic": "Value Putting"
    },
    "Aptitude > Algebra > Square Root of Irrational Numbers": {
        "subject": "Aptitude",
        "topic": "Algebra",
        "subtopic": "Square Root of Irrational Numbers"
    },
    "Aptitude > Algebra > Componendo - Dividendo": {
        "subject": "Aptitude",
        "topic": "Algebra",
        "subtopic": "Componendo - Dividendo"
    },
    "Aptitude > Geometry > Types of Angles": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Types of Angles"
    },
    "Aptitude > Geometry > Lines & Angles Concepts": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Lines & Angles Concepts"
    },
    "Aptitude > Geometry > Triangles-Properties of a Triangle": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Triangles-Properties of a Triangle"
    },
    "Aptitude > Geometry > Triangles-Exterior Angle Property": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Triangles-Exterior Angle Property"
    },
    "Aptitude > Geometry > Triangles-Basic Question": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Triangles-Basic Question"
    },
    "Aptitude > Geometry > Condition for formation of a Triangle": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Condition for formation of a Triangle"
    },
    "Aptitude > Geometry > Sine Rule": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Sine Rule"
    },
    "Aptitude > Geometry > Triangles-Stewart’s Theorem": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Triangles-Stewart’s Theorem"
    },
    "Aptitude > Geometry > Triangles-Internal bisector": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Triangles-Internal bisector"
    },
    "Aptitude > Geometry > Types of Triangle": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Types of Triangle"
    },
    "Aptitude > Geometry > Isosceles Triangle": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Isosceles Triangle"
    },
    "Aptitude > Geometry > Equilateral Triangle": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Equilateral Triangle"
    },
    "Aptitude > Geometry > Triangles-On the basis of Angles": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Triangles-On the basis of Angles"
    },
    "Aptitude > Geometry > Congruent Triangle": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Congruent Triangle"
    },
    "Aptitude > Geometry > Triangles-Similarity": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Triangles-Similarity"
    },
    "Aptitude > Geometry > Similarity of Right Angle Triangle": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Similarity of Right Angle Triangle"
    },
    "Aptitude > Geometry > Basic Proportionality Theorem": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Basic Proportionality Theorem"
    },
    "Aptitude > Geometry > Centers of Triangle": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Centers of Triangle"
    },
    "Aptitude > Geometry > Median Property": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Median Property"
    },
    "Aptitude > Geometry > Apollonius's Theorem": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Apollonius's Theorem"
    },
    "Aptitude > Geometry > Median in a Right-Angled Triangle": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Median in a Right-Angled Triangle"
    },
    "Aptitude > Geometry > Incentre": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Incentre"
    },
    "Aptitude > Geometry > Inradius": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Inradius"
    },
    "Aptitude > Geometry > Ex-Circle": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Ex-Circle"
    },
    "Aptitude > Geometry > Circumcenter": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Circumcenter"
    },
    "Aptitude > Geometry > Circumcentre in Triangles": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Circumcentre in Triangles"
    },
    "Aptitude > Geometry > Circumcentre in Right Angle Triangle": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Circumcentre in Right Angle Triangle"
    },
    "Aptitude > Geometry > Orthocentre": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Orthocentre"
    },
    "Aptitude > Geometry > Orthocentre - Height and Side Ratio": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Orthocentre - Height and Side Ratio"
    },
    "Aptitude > Geometry > Orthocenter - Altitude in Terms of the Sides": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Orthocenter - Altitude in Terms of the Sides"
    },
    "Aptitude > Geometry > Interior Angle Bisector Theorem": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Interior Angle Bisector Theorem"
    },
    "Aptitude > Geometry > Length of Angle Bisector": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Length of Angle Bisector"
    },
    "Aptitude > Geometry > Mass Point Geometry": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Mass Point Geometry"
    },
    "Aptitude > Geometry > Circle - Chord": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Circle - Chord"
    },
    "Aptitude > Geometry > Circles - Property": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Circles - Property"
    },
    "Aptitude > Geometry > Circles - Basic question": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Circles - Basic question"
    },
    "Aptitude > Geometry > Circles - Two chords": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Circles - Two chords"
    },
    "Aptitude > Geometry > Circles - Secants intersect": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Circles - Secants intersect"
    },
    "Aptitude > Geometry > Circles - Secants & Tangent": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Circles - Secants & Tangent"
    },
    "Aptitude > Geometry > Circles - Length of the Chord": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Circles - Length of the Chord"
    },
    "Aptitude > Geometry > Circles - Two Parallel Chords": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Circles - Two Parallel Chords"
    },
    "Aptitude > Geometry > Circles - Tangent": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Circles - Tangent"
    },
    "Aptitude > Geometry > Circles - Alternate Segment Theorem": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Circles - Alternate Segment Theorem"
    },
    "Aptitude > Geometry > Circles - Circumscribing a circle": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Circles - Circumscribing a circle"
    },
    "Aptitude > Geometry > Circle -Touch Externally": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Circle -Touch Externally"
    },
    "Aptitude > Geometry > Circle - Intersect each other": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Circle - Intersect each other"
    },
    "Aptitude > Geometry > Circle - Intersecting Circles": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Circle - Intersecting Circles"
    },
    "Aptitude > Geometry > Circle - Concentric Circles": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Circle - Concentric Circles"
    },
    "Aptitude > Geometry > Circle - Touch Externally": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Circle - Touch Externally"
    },
    "Aptitude > Geometry > Circle - three circle with radii": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Circle - three circle with radii"
    },
    "Aptitude > Geometry > Direct Common Tangent": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Direct Common Tangent"
    },
    "Aptitude > Geometry > Transverse Common Tangent": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Transverse Common Tangent"
    },
    "Aptitude > Geometry > Circle- two circle intersecting internally": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Circle- two circle intersecting internally"
    },
    "Aptitude > Geometry > Cyclic Quadrilateral": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Cyclic Quadrilateral"
    },
    "Aptitude > Geometry > Area of Cyclic Quadrilateral": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Area of Cyclic Quadrilateral"
    },
    "Aptitude > Geometry > Quadrilateral": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Quadrilateral"
    },
    "Aptitude > Geometry > Quadrilateral-Types": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Quadrilateral-Types"
    },
    "Aptitude > Geometry > Parallelogram": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Parallelogram"
    },
    "Aptitude > Geometry > Rectangle": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Rectangle"
    },
    "Aptitude > Geometry > Square": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Square"
    },
    "Aptitude > Geometry > Rhombus": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Rhombus"
    },
    "Aptitude > Geometry > Trapezium": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Trapezium"
    },
    "Aptitude > Geometry > Polygon": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Polygon"
    },
    "Aptitude > Geometry > Angles of polygon": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Angles of polygon"
    },
    "Aptitude > Geometry > Area of Regular Polygon": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Area of Regular Polygon"
    },
    "Aptitude > Geometry > Hexagon": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Hexagon"
    },
    "Aptitude > Geometry > Hexagon-Equal Divisions of Area": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Hexagon-Equal Divisions of Area"
    },
    "Aptitude > Geometry > Hexagon-Basic Question": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Hexagon-Basic Question"
    },
    "Aptitude > Geometry > Octagon": {
        "subject": "Aptitude",
        "topic": "Geometry",
        "subtopic": "Octagon"
    },
    "Aptitude > Coordinate Geometry > Distance between Two Points": {
        "subject": "Aptitude",
        "topic": "Coordinate Geometry",
        "subtopic": "Distance between Two Points"
    },
    "Aptitude > Coordinate Geometry > Section of a Line": {
        "subject": "Aptitude",
        "topic": "Coordinate Geometry",
        "subtopic": "Section of a Line"
    },
    "Aptitude > Coordinate Geometry > Slope of a Line": {
        "subject": "Aptitude",
        "topic": "Coordinate Geometry",
        "subtopic": "Slope of a Line"
    },
    "Aptitude > Coordinate Geometry > Angle between Two Lines": {
        "subject": "Aptitude",
        "topic": "Coordinate Geometry",
        "subtopic": "Angle between Two Lines"
    },
    "Aptitude > Coordinate Geometry > Equation of lines": {
        "subject": "Aptitude",
        "topic": "Coordinate Geometry",
        "subtopic": "Equation of lines"
    },
    "Aptitude > Coordinate Geometry > Distance of a Point from a Line": {
        "subject": "Aptitude",
        "topic": "Coordinate Geometry",
        "subtopic": "Distance of a Point from a Line"
    },
    "Aptitude > Coordinate Geometry > Distance between Parallel Lines": {
        "subject": "Aptitude",
        "topic": "Coordinate Geometry",
        "subtopic": "Distance between Parallel Lines"
    },
    "Aptitude > Coordinate Geometry > Reflection of a Point": {
        "subject": "Aptitude",
        "topic": "Coordinate Geometry",
        "subtopic": "Reflection of a Point"
    },
    "Aptitude > Mensuration > Polygons": {
        "subject": "Aptitude",
        "topic": "Mensuration",
        "subtopic": "Polygons"
    },
    "Aptitude > Mensuration > Triangles": {
        "subject": "Aptitude",
        "topic": "Mensuration",
        "subtopic": "Triangles"
    },
    "Aptitude > Mensuration > Classification of Triangles": {
        "subject": "Aptitude",
        "topic": "Mensuration",
        "subtopic": "Classification of Triangles"
    },
    "Aptitude > Mensuration > Area and Perimeter of Triangle": {
        "subject": "Aptitude",
        "topic": "Mensuration",
        "subtopic": "Area and Perimeter of Triangle"
    },
    "Aptitude > Mensuration > Area of cyclic Quadrilateral": {
        "subject": "Aptitude",
        "topic": "Mensuration",
        "subtopic": "Area of cyclic Quadrilateral"
    },
    "Aptitude > Mensuration > Square": {
        "subject": "Aptitude",
        "topic": "Mensuration",
        "subtopic": "Square"
    },
    "Aptitude > Mensuration > Rectangle": {
        "subject": "Aptitude",
        "topic": "Mensuration",
        "subtopic": "Rectangle"
    },
    "Aptitude > Mensuration > Rhombus": {
        "subject": "Aptitude",
        "topic": "Mensuration",
        "subtopic": "Rhombus"
    },
    "Aptitude > Mensuration > Parallelogram": {
        "subject": "Aptitude",
        "topic": "Mensuration",
        "subtopic": "Parallelogram"
    },
    "Aptitude > Mensuration > Trapezium": {
        "subject": "Aptitude",
        "topic": "Mensuration",
        "subtopic": "Trapezium"
    },
    "Aptitude > Mensuration > Hexagon": {
        "subject": "Aptitude",
        "topic": "Mensuration",
        "subtopic": "Hexagon"
    },
    "Aptitude > Mensuration > Octagon": {
        "subject": "Aptitude",
        "topic": "Mensuration",
        "subtopic": "Octagon"
    },
    "Aptitude > Mensuration > Circle": {
        "subject": "Aptitude",
        "topic": "Mensuration",
        "subtopic": "Circle"
    },
    "Aptitude > Mensuration > Ratio of Radius, Perimeter & Area of Circle": {
        "subject": "Aptitude",
        "topic": "Mensuration",
        "subtopic": "Ratio of Radius, Perimeter & Area of Circle"
    },
    "Aptitude > Mensuration > Circular Ring": {
        "subject": "Aptitude",
        "topic": "Mensuration",
        "subtopic": "Circular Ring"
    },
    "Aptitude > Mensuration > Area and Perimeter of Semi Circle & Quarter Circle": {
        "subject": "Aptitude",
        "topic": "Mensuration",
        "subtopic": "Area and Perimeter of Semi Circle & Quarter Circle"
    },
    "Aptitude > Mensuration > Sector of a Circle": {
        "subject": "Aptitude",
        "topic": "Mensuration",
        "subtopic": "Sector of a Circle"
    },
    "Aptitude > Mensuration > Square and Circle": {
        "subject": "Aptitude",
        "topic": "Mensuration",
        "subtopic": "Square and Circle"
    },
    "Aptitude > Mensuration > Triangles & Circles": {
        "subject": "Aptitude",
        "topic": "Mensuration",
        "subtopic": "Triangles & Circles"
    },
    "Aptitude > Mensuration > Square, Rectangle & Triangle": {
        "subject": "Aptitude",
        "topic": "Mensuration",
        "subtopic": "Square, Rectangle & Triangle"
    },
    "Aptitude > Mensuration > Same perimeter": {
        "subject": "Aptitude",
        "topic": "Mensuration",
        "subtopic": "Same perimeter"
    },
    "Aptitude > Mensuration > Rectangle path": {
        "subject": "Aptitude",
        "topic": "Mensuration",
        "subtopic": "Rectangle path"
    },
    "Aptitude > Mensuration > Cost based on Area & Perimeter": {
        "subject": "Aptitude",
        "topic": "Mensuration",
        "subtopic": "Cost based on Area & Perimeter"
    },
    "Aptitude > Mensuration > Band Around Circles": {
        "subject": "Aptitude",
        "topic": "Mensuration",
        "subtopic": "Band Around Circles"
    },
    "Aptitude > Mensuration > Prism": {
        "subject": "Aptitude",
        "topic": "Mensuration",
        "subtopic": "Prism"
    },
    "Aptitude > Mensuration > Cube": {
        "subject": "Aptitude",
        "topic": "Mensuration",
        "subtopic": "Cube"
    },
    "Aptitude > Mensuration > Cuboid": {
        "subject": "Aptitude",
        "topic": "Mensuration",
        "subtopic": "Cuboid"
    },
    "Aptitude > Mensuration > Right Circular Cylinder": {
        "subject": "Aptitude",
        "topic": "Mensuration",
        "subtopic": "Right Circular Cylinder"
    },
    "Aptitude > Mensuration > Pyramid": {
        "subject": "Aptitude",
        "topic": "Mensuration",
        "subtopic": "Pyramid"
    },
    "Aptitude > Mensuration > Cone": {
        "subject": "Aptitude",
        "topic": "Mensuration",
        "subtopic": "Cone"
    },
    "Aptitude > Mensuration > Frustom of a Cone": {
        "subject": "Aptitude",
        "topic": "Mensuration",
        "subtopic": "Frustom of a Cone"
    },
    "Aptitude > Mensuration > Ratio of Volume of Pyramid": {
        "subject": "Aptitude",
        "topic": "Mensuration",
        "subtopic": "Ratio of Volume of Pyramid"
    },
    "Aptitude > Mensuration > Sphere": {
        "subject": "Aptitude",
        "topic": "Mensuration",
        "subtopic": "Sphere"
    },
    "Aptitude > Mensuration > Hollow Sphere": {
        "subject": "Aptitude",
        "topic": "Mensuration",
        "subtopic": "Hollow Sphere"
    },
    "Aptitude > Mensuration > Hemisphere": {
        "subject": "Aptitude",
        "topic": "Mensuration",
        "subtopic": "Hemisphere"
    },
    "Aptitude > Mensuration > Relation between Volumes of Cylinder, Cone and Hemisphere": {
        "subject": "Aptitude",
        "topic": "Mensuration",
        "subtopic": "Relation between Volumes of Cylinder, Cone and Hemisphere"
    },
    "Aptitude > Mensuration > Conversion of Solids from One Form to Another": {
        "subject": "Aptitude",
        "topic": "Mensuration",
        "subtopic": "Conversion of Solids from One Form to Another"
    },
    "Aptitude > Mensuration > Area or Volume after Removal of Solids": {
        "subject": "Aptitude",
        "topic": "Mensuration",
        "subtopic": "Area or Volume after Removal of Solids"
    },
    "Aptitude > Mensuration > Volume of Water Flowing from a Pipe": {
        "subject": "Aptitude",
        "topic": "Mensuration",
        "subtopic": "Volume of Water Flowing from a Pipe"
    },
    "Aptitude > Mensuration > Useful Results": {
        "subject": "Aptitude",
        "topic": "Mensuration",
        "subtopic": "Useful Results"
    },
    "Aptitude > Mensuration > One Figure inside Another": {
        "subject": "Aptitude",
        "topic": "Mensuration",
        "subtopic": "One Figure inside Another"
    },
    "Aptitude > Mensuration > Figure Based Questions": {
        "subject": "Aptitude",
        "topic": "Mensuration",
        "subtopic": "Figure Based Questions"
    },
    "Aptitude > Trigonometry > Trigonometry circular measure of angles": {
        "subject": "Aptitude",
        "topic": "Trigonometry",
        "subtopic": "Trigonometry circular measure of angles"
    },
    "Aptitude > Trigonometry > Circular system": {
        "subject": "Aptitude",
        "topic": "Trigonometry",
        "subtopic": "Circular system"
    },
    "Aptitude > Trigonometry > Basic Identities of Trigonometry": {
        "subject": "Aptitude",
        "topic": "Trigonometry",
        "subtopic": "Basic Identities of Trigonometry"
    },
    "Aptitude > Trigonometry > Trigonometric Ratios of some specific angles": {
        "subject": "Aptitude",
        "topic": "Trigonometry",
        "subtopic": "Trigonometric Ratios of some specific angles"
    },
    "Aptitude > Trigonometry > Quadrant System": {
        "subject": "Aptitude",
        "topic": "Trigonometry",
        "subtopic": "Quadrant System"
    },
    "Aptitude > Trigonometry > Sum of two angles (𝛼+𝛽)=90": {
        "subject": "Aptitude",
        "topic": "Trigonometry",
        "subtopic": "Sum of two angles (𝛼+𝛽)=90"
    },
    "Aptitude > Trigonometry > Basic Identities": {
        "subject": "Aptitude",
        "topic": "Trigonometry",
        "subtopic": "Basic Identities"
    },
    "Aptitude > Trigonometry > Based on Putting Value": {
        "subject": "Aptitude",
        "topic": "Trigonometry",
        "subtopic": "Based on Putting Value"
    },
    "Aptitude > Trigonometry > x+1/x=2": {
        "subject": "Aptitude",
        "topic": "Trigonometry",
        "subtopic": "x+1/x=2"
    },
    "Aptitude > Trigonometry > Basic Identity (compound angles)": {
        "subject": "Aptitude",
        "topic": "Trigonometry",
        "subtopic": "Basic Identity (compound angles)"
    },
    "Aptitude > Trigonometry > Maximum & minimum value of trigonometrix": {
        "subject": "Aptitude",
        "topic": "Trigonometry",
        "subtopic": "Maximum & minimum value of trigonometrix"
    },
    "Aptitude > Height & Distance > Height & Distance - Basic concept": {
        "subject": "Aptitude",
        "topic": "Height & Distance",
        "subtopic": "Height & Distance - Basic concept"
    },
    "Aptitude > Height & Distance > Based on Angle Changed:": {
        "subject": "Aptitude",
        "topic": "Height & Distance",
        "subtopic": "Based on Angle Changed:"
    },
    "Aptitude > Height & Distance > Height & Distance - Complementary Angle": {
        "subject": "Aptitude",
        "topic": "Height & Distance",
        "subtopic": "Height & Distance - Complementary Angle"
    },
    "Aptitude > Probability > Probability": {
        "subject": "Aptitude",
        "topic": "Probability",
        "subtopic": "Probability"
    },
    "Aptitude > Statistics > Class intervals , Frequency": {
        "subject": "Aptitude",
        "topic": "Statistics",
        "subtopic": "Class intervals , Frequency"
    },
    "Aptitude > Statistics > Mean,Mode,Median": {
        "subject": "Aptitude",
        "topic": "Statistics",
        "subtopic": "Mean,Mode,Median"
    },
    "English > Noun > Noun": {
        "subject": "English",
        "topic": "Noun",
        "subtopic": "Noun"
    },
    "English > Noun > Types of Nouns": {
        "subject": "English",
        "topic": "Noun",
        "subtopic": "Types of Nouns"
    },
    "English > Noun > Countable and Uncountable": {
        "subject": "English",
        "topic": "Noun",
        "subtopic": "Countable and Uncountable"
    },
    "English > Noun > Rules Based on Numbers": {
        "subject": "English",
        "topic": "Noun",
        "subtopic": "Rules Based on Numbers"
    },
    "English > Noun > Based on Gender": {
        "subject": "English",
        "topic": "Noun",
        "subtopic": "Based on Gender"
    },
    "English > Noun > Based On Noun - Case": {
        "subject": "English",
        "topic": "Noun",
        "subtopic": "Based On Noun - Case"
    },
    "English > Noun > Confusing Words": {
        "subject": "English",
        "topic": "Noun",
        "subtopic": "Confusing Words"
    },
    "English > Noun > Find the Correct One": {
        "subject": "English",
        "topic": "Noun",
        "subtopic": "Find the Correct One"
    },
    "English > Pronoun > Pronoun": {
        "subject": "English",
        "topic": "Pronoun",
        "subtopic": "Pronoun"
    },
    "English > Pronoun > Rules Based on Possessive Pronoun": {
        "subject": "English",
        "topic": "Pronoun",
        "subtopic": "Rules Based on Possessive Pronoun"
    },
    "English > Pronoun > Relative Pronoun": {
        "subject": "English",
        "topic": "Pronoun",
        "subtopic": "Relative Pronoun"
    },
    "English > Pronoun > Reciprocal Pronoun": {
        "subject": "English",
        "topic": "Pronoun",
        "subtopic": "Reciprocal Pronoun"
    },
    "English > Pronoun > Pronoun Workout": {
        "subject": "English",
        "topic": "Pronoun",
        "subtopic": "Pronoun Workout"
    },
    "English > Verb > Forms of Verb": {
        "subject": "English",
        "topic": "Verb",
        "subtopic": "Forms of Verb"
    },
    "English > Verb > Regular Verbs": {
        "subject": "English",
        "topic": "Verb",
        "subtopic": "Regular Verbs"
    },
    "English > Verb > Modal verbs": {
        "subject": "English",
        "topic": "Verb",
        "subtopic": "Modal verbs"
    },
    "English > Verb > Rules Based on Verbs": {
        "subject": "English",
        "topic": "Verb",
        "subtopic": "Rules Based on Verbs"
    },
    "English > Adverb > Adverb": {
        "subject": "English",
        "topic": "Adverb",
        "subtopic": "Adverb"
    },
    "English > Adverb > Adverb of Place": {
        "subject": "English",
        "topic": "Adverb",
        "subtopic": "Adverb of Place"
    },
    "English > Adverb > Rules for Adverb": {
        "subject": "English",
        "topic": "Adverb",
        "subtopic": "Rules for Adverb"
    },
    "English > Adverb > workouts": {
        "subject": "English",
        "topic": "Adverb",
        "subtopic": "workouts"
    },
    "English > Tenses > Tenses": {
        "subject": "English",
        "topic": "Tenses",
        "subtopic": "Tenses"
    },
    "English > Adjectives > Distributive Adjectives": {
        "subject": "English",
        "topic": "Adjectives",
        "subtopic": "Distributive Adjectives"
    },
    "English > Adjectives > Rules - Degrees of Comparison": {
        "subject": "English",
        "topic": "Adjectives",
        "subtopic": "Rules - Degrees of Comparison"
    },
    "English > Prepositions > Prepositions": {
        "subject": "English",
        "topic": "Prepositions",
        "subtopic": "Prepositions"
    },
    "English > Subject Verb Agreement > Rule 1-5": {
        "subject": "English",
        "topic": "Subject Verb Agreement",
        "subtopic": "Rule 1-5"
    },
    "English > Subject Verb Agreement > Rule 06-12": {
        "subject": "English",
        "topic": "Subject Verb Agreement",
        "subtopic": "Rule 06-12"
    },
    "English > Subject Verb Agreement > Rule 13-19": {
        "subject": "English",
        "topic": "Subject Verb Agreement",
        "subtopic": "Rule 13-19"
    },
    "English > Subject Verb Agreement > Rule 20-24": {
        "subject": "English",
        "topic": "Subject Verb Agreement",
        "subtopic": "Rule 20-24"
    },
    "English > Subject Verb Agreement > Rule 25-28": {
        "subject": "English",
        "topic": "Subject Verb Agreement",
        "subtopic": "Rule 25-28"
    },
    "English > Subject Verb Agreement > Sentence Improvement & Error Spotting": {
        "subject": "English",
        "topic": "Subject Verb Agreement",
        "subtopic": "Sentence Improvement & Error Spotting"
    },
    "English > Articles > Articles-Use of a/an": {
        "subject": "English",
        "topic": "Articles",
        "subtopic": "Articles-Use of a/an"
    },
    "English > Articles > Articles-Use of The": {
        "subject": "English",
        "topic": "Articles",
        "subtopic": "Articles-Use of The"
    },
    "English > Articles > Omission": {
        "subject": "English",
        "topic": "Articles",
        "subtopic": "Omission"
    },
    "English > Articles > exercise": {
        "subject": "English",
        "topic": "Articles",
        "subtopic": "exercise"
    },
    "English > Conjunction > Co-ordinating Conjunctions": {
        "subject": "English",
        "topic": "Conjunction",
        "subtopic": "Co-ordinating Conjunctions"
    },
    "English > Conjunction > Subordinating Conjunction": {
        "subject": "English",
        "topic": "Conjunction",
        "subtopic": "Subordinating Conjunction"
    },
    "English > Conjunction > Subordinating conjunctions & Correlative conjunctions": {
        "subject": "English",
        "topic": "Conjunction",
        "subtopic": "Subordinating conjunctions & Correlative conjunctions"
    },
    "English > Conjunction > Rules": {
        "subject": "English",
        "topic": "Conjunction",
        "subtopic": "Rules"
    },
    "English > Speech > Sentence types": {
        "subject": "English",
        "topic": "Speech",
        "subtopic": "Sentence types"
    },
    "English > Speech > Change of Persons": {
        "subject": "English",
        "topic": "Speech",
        "subtopic": "Change of Persons"
    },
    "English > Speech > Change of Time": {
        "subject": "English",
        "topic": "Speech",
        "subtopic": "Change of Time"
    },
    "English > Speech > Change of Time-Type 2": {
        "subject": "English",
        "topic": "Speech",
        "subtopic": "Change of Time-Type 2"
    },
    "English > Speech > Other Parts of Speech and Assertive Sentence": {
        "subject": "English",
        "topic": "Speech",
        "subtopic": "Other Parts of Speech and Assertive Sentence"
    },
    "English > Speech > Interrogative Sentence": {
        "subject": "English",
        "topic": "Speech",
        "subtopic": "Interrogative Sentence"
    },
    "English > Speech > Imperative Sentence": {
        "subject": "English",
        "topic": "Speech",
        "subtopic": "Imperative Sentence"
    },
    "English > Speech > Optative and Exclamatory Sentences": {
        "subject": "English",
        "topic": "Speech",
        "subtopic": "Optative and Exclamatory Sentences"
    },
    "English > Speech > Previous year Question": {
        "subject": "English",
        "topic": "Speech",
        "subtopic": "Previous year Question"
    },
    "English > Speech > Revision": {
        "subject": "English",
        "topic": "Speech",
        "subtopic": "Revision"
    },
    "English > Voice > 5 Rules": {
        "subject": "English",
        "topic": "Voice",
        "subtopic": "5 Rules"
    },
    "English > Voice > Passive Formation of the Types of Tenses": {
        "subject": "English",
        "topic": "Voice",
        "subtopic": "Passive Formation of the Types of Tenses"
    },
    "English > Voice > Continous tense": {
        "subject": "English",
        "topic": "Voice",
        "subtopic": "Continous tense"
    },
    "English > Voice > Perfect tense": {
        "subject": "English",
        "topic": "Voice",
        "subtopic": "Perfect tense"
    },
    "English > Voice > Modal auxillary verb": {
        "subject": "English",
        "topic": "Voice",
        "subtopic": "Modal auxillary verb"
    },
    "English > Voice > Imperative": {
        "subject": "English",
        "topic": "Voice",
        "subtopic": "Imperative"
    },
    "English > Voice > Interrogative": {
        "subject": "English",
        "topic": "Voice",
        "subtopic": "Interrogative"
    },
    "English > Voice > Prepositions": {
        "subject": "English",
        "topic": "Voice",
        "subtopic": "Prepositions"
    },
    "English > Voice > Miscellaneous": {
        "subject": "English",
        "topic": "Voice",
        "subtopic": "Miscellaneous"
    },
    "English > Voice > Exercise": {
        "subject": "English",
        "topic": "Voice",
        "subtopic": "Exercise"
    },
    "English > Reading Comprehension > Questions": {
        "subject": "English",
        "topic": "Reading Comprehension",
        "subtopic": "Questions"
    },
    "English > Cloze Test > Cloze Test": {
        "subject": "English",
        "topic": "Cloze Test",
        "subtopic": "Cloze Test"
    },
    "English > Synonyms & Antonyms > Synonyms": {
        "subject": "English",
        "topic": "Synonyms & Antonyms",
        "subtopic": "Synonyms"
    },
    "English > Synonyms & Antonyms > Antonyms": {
        "subject": "English",
        "topic": "Synonyms & Antonyms",
        "subtopic": "Antonyms"
    },
    "English > One Word Substitution > One Word Substitution": {
        "subject": "English",
        "topic": "One Word Substitution",
        "subtopic": "One Word Substitution"
    },
    "English > Idioms & Phrases > Basics": {
        "subject": "English",
        "topic": "Idioms & Phrases",
        "subtopic": "Basics"
    },
    "English > Idioms & Phrases > Idiom-based on weather": {
        "subject": "English",
        "topic": "Idioms & Phrases",
        "subtopic": "Idiom-based on weather"
    },
    "English > Idioms & Phrases > Idiom-based on colour": {
        "subject": "English",
        "topic": "Idioms & Phrases",
        "subtopic": "Idiom-based on colour"
    },
    "English > Idioms & Phrases > Idiom-based on body parts": {
        "subject": "English",
        "topic": "Idioms & Phrases",
        "subtopic": "Idiom-based on body parts"
    },
    "English > Idioms & Phrases > Idiom-based on numbers": {
        "subject": "English",
        "topic": "Idioms & Phrases",
        "subtopic": "Idiom-based on numbers"
    },
    "English > Idioms & Phrases > Phrasal Verbs": {
        "subject": "English",
        "topic": "Idioms & Phrases",
        "subtopic": "Phrasal Verbs"
    },
    "English > Question Tag > Rules 1-5": {
        "subject": "English",
        "topic": "Question Tag",
        "subtopic": "Rules 1-5"
    },
    "English > Question Tag > Rules 6-11": {
        "subject": "English",
        "topic": "Question Tag",
        "subtopic": "Rules 6-11"
    },
    "English > Question Tag > Exercise": {
        "subject": "English",
        "topic": "Question Tag",
        "subtopic": "Exercise"
    },
    "English > Conditional Clauses > Zero and first": {
        "subject": "English",
        "topic": "Conditional Clauses",
        "subtopic": "Zero and first"
    },
    "English > Conditional Clauses > Second & three Conditional": {
        "subject": "English",
        "topic": "Conditional Clauses",
        "subtopic": "Second & three Conditional"
    },
    "English > Conditional Clauses > Mixed and Unless": {
        "subject": "English",
        "topic": "Conditional Clauses",
        "subtopic": "Mixed and Unless"
    },
    "English > Conditional Clauses > Spot the Error": {
        "subject": "English",
        "topic": "Conditional Clauses",
        "subtopic": "Spot the Error"
    },
    "General Studies > Ancient - History > Prehistoric And Indus Valley": {
        "subject": "General Studies",
        "topic": "Ancient - History",
        "subtopic": "Prehistoric And Indus Valley"
    },
    "General Studies > Ancient - History > Vedic Age": {
        "subject": "General Studies",
        "topic": "Ancient - History",
        "subtopic": "Vedic Age"
    },
    "General Studies > Ancient - History > Jainism": {
        "subject": "General Studies",
        "topic": "Ancient - History",
        "subtopic": "Jainism"
    },
    "General Studies > Ancient - History > Buddhism": {
        "subject": "General Studies",
        "topic": "Ancient - History",
        "subtopic": "Buddhism"
    },
    "General Studies > Ancient - History > Mahajanapadas": {
        "subject": "General Studies",
        "topic": "Ancient - History",
        "subtopic": "Mahajanapadas"
    },
    "General Studies > Ancient - History > Mauryan Dynasty": {
        "subject": "General Studies",
        "topic": "Ancient - History",
        "subtopic": "Mauryan Dynasty"
    },
    "General Studies > Ancient - History > Gupta Dynasty": {
        "subject": "General Studies",
        "topic": "Ancient - History",
        "subtopic": "Gupta Dynasty"
    },
    "General Studies > Ancient - History > Vardhana Dynasty": {
        "subject": "General Studies",
        "topic": "Ancient - History",
        "subtopic": "Vardhana Dynasty"
    },
    "General Studies > Ancient - History > sangam": {
        "subject": "General Studies",
        "topic": "Ancient - History",
        "subtopic": "sangam"
    },
    "General Studies > Ancient - History > Chola Dynasty": {
        "subject": "General Studies",
        "topic": "Ancient - History",
        "subtopic": "Chola Dynasty"
    },
    "General Studies > Ancient - History > Pallavas": {
        "subject": "General Studies",
        "topic": "Ancient - History",
        "subtopic": "Pallavas"
    },
    "General Studies > Ancient - History > Saka Era": {
        "subject": "General Studies",
        "topic": "Ancient - History",
        "subtopic": "Saka Era"
    },
    "General Studies > Ancient - History > Kushanas": {
        "subject": "General Studies",
        "topic": "Ancient - History",
        "subtopic": "Kushanas"
    },
    "General Studies > Medieval - History > Foreign Invasions": {
        "subject": "General Studies",
        "topic": "Medieval - History",
        "subtopic": "Foreign Invasions"
    },
    "General Studies > Medieval - History > Delhi Sultanate": {
        "subject": "General Studies",
        "topic": "Medieval - History",
        "subtopic": "Delhi Sultanate"
    },
    "General Studies > Medieval - History > Slave Dynasty": {
        "subject": "General Studies",
        "topic": "Medieval - History",
        "subtopic": "Slave Dynasty"
    },
    "General Studies > Medieval - History > Khilji Dynasty": {
        "subject": "General Studies",
        "topic": "Medieval - History",
        "subtopic": "Khilji Dynasty"
    },
    "General Studies > Medieval - History > Tughlaq Dynasty": {
        "subject": "General Studies",
        "topic": "Medieval - History",
        "subtopic": "Tughlaq Dynasty"
    },
    "General Studies > Medieval - History > Sayyid Dynasty": {
        "subject": "General Studies",
        "topic": "Medieval - History",
        "subtopic": "Sayyid Dynasty"
    },
    "General Studies > Medieval - History > Lodi Dynasty": {
        "subject": "General Studies",
        "topic": "Medieval - History",
        "subtopic": "Lodi Dynasty"
    },
    "General Studies > Medieval - History > Mughal Period": {
        "subject": "General Studies",
        "topic": "Medieval - History",
        "subtopic": "Mughal Period"
    },
    "General Studies > Medieval - History > Babur": {
        "subject": "General Studies",
        "topic": "Medieval - History",
        "subtopic": "Babur"
    },
    "General Studies > Medieval - History > Humayun and Sher Shah Suri": {
        "subject": "General Studies",
        "topic": "Medieval - History",
        "subtopic": "Humayun and Sher Shah Suri"
    },
    "General Studies > Medieval - History > Akbar": {
        "subject": "General Studies",
        "topic": "Medieval - History",
        "subtopic": "Akbar"
    },
    "General Studies > Medieval - History > Jahangir": {
        "subject": "General Studies",
        "topic": "Medieval - History",
        "subtopic": "Jahangir"
    },
    "General Studies > Medieval - History > Shah Jahan": {
        "subject": "General Studies",
        "topic": "Medieval - History",
        "subtopic": "Shah Jahan"
    },
    "General Studies > Medieval - History > Aurangzeb": {
        "subject": "General Studies",
        "topic": "Medieval - History",
        "subtopic": "Aurangzeb"
    },
    "General Studies > Medieval - History > Sufism": {
        "subject": "General Studies",
        "topic": "Medieval - History",
        "subtopic": "Sufism"
    },
    "General Studies > Medieval - History > Sikh Guru": {
        "subject": "General Studies",
        "topic": "Medieval - History",
        "subtopic": "Sikh Guru"
    },
    "General Studies > Medieval - History > Maratha Empire": {
        "subject": "General Studies",
        "topic": "Medieval - History",
        "subtopic": "Maratha Empire"
    },
    "General Studies > Medieval - History > Vijaynagar Empire": {
        "subject": "General Studies",
        "topic": "Medieval - History",
        "subtopic": "Vijaynagar Empire"
    },
    "General Studies > Medieval - History > Wars and Treaties": {
        "subject": "General Studies",
        "topic": "Medieval - History",
        "subtopic": "Wars and Treaties"
    },
    "General Studies > Medieval - History > Miscellaneous": {
        "subject": "General Studies",
        "topic": "Medieval - History",
        "subtopic": "Miscellaneous"
    },
    "General Studies > Modern - History > The Revolt of 1857": {
        "subject": "General Studies",
        "topic": "Modern - History",
        "subtopic": "The Revolt of 1857"
    },
    "General Studies > Modern - History > Governors and Viceroys": {
        "subject": "General Studies",
        "topic": "Modern - History",
        "subtopic": "Governors and Viceroys"
    },
    "General Studies > Modern - History > British acts and Policies": {
        "subject": "General Studies",
        "topic": "Modern - History",
        "subtopic": "British acts and Policies"
    },
    "General Studies > Modern - History > Partition of Bengal and Swadeshi Movements": {
        "subject": "General Studies",
        "topic": "Modern - History",
        "subtopic": "Partition of Bengal and Swadeshi Movements"
    },
    "General Studies > Modern - History > Gandhian Era": {
        "subject": "General Studies",
        "topic": "Modern - History",
        "subtopic": "Gandhian Era"
    },
    "General Studies > Modern - History > Expansion of British Rule": {
        "subject": "General Studies",
        "topic": "Modern - History",
        "subtopic": "Expansion of British Rule"
    },
    "General Studies > Modern - History > The Revolutionaries": {
        "subject": "General Studies",
        "topic": "Modern - History",
        "subtopic": "The Revolutionaries"
    },
    "General Studies > Modern - History > Struggle for Independence": {
        "subject": "General Studies",
        "topic": "Modern - History",
        "subtopic": "Struggle for Independence"
    },
    "General Studies > Modern - History > Socio Religious Reforms": {
        "subject": "General Studies",
        "topic": "Modern - History",
        "subtopic": "Socio Religious Reforms"
    },
    "General Studies > Modern - History > Indian National Congress and Its Sessions": {
        "subject": "General Studies",
        "topic": "Modern - History",
        "subtopic": "Indian National Congress and Its Sessions"
    },
    "General Studies > Modern - History > Muslim league": {
        "subject": "General Studies",
        "topic": "Modern - History",
        "subtopic": "Muslim league"
    },
    "General Studies > Modern - History > Leaders": {
        "subject": "General Studies",
        "topic": "Modern - History",
        "subtopic": "Leaders"
    },
    "General Studies > Modern - History > Miscellaneous": {
        "subject": "General Studies",
        "topic": "Modern - History",
        "subtopic": "Miscellaneous"
    },
    "General Studies > Geography > Solar system and its planets": {
        "subject": "General Studies",
        "topic": "Geography",
        "subtopic": "Solar system and its planets"
    },
    "General Studies > Geography > Longitudes and latitudes": {
        "subject": "General Studies",
        "topic": "Geography",
        "subtopic": "Longitudes and latitudes"
    },
    "General Studies > Geography > Continents and Oceans": {
        "subject": "General Studies",
        "topic": "Geography",
        "subtopic": "Continents and Oceans"
    },
    "General Studies > Geography > Neighbouring Countries of India": {
        "subject": "General Studies",
        "topic": "Geography",
        "subtopic": "Neighbouring Countries of India"
    },
    "General Studies > Geography > Indian Drainage System": {
        "subject": "General Studies",
        "topic": "Geography",
        "subtopic": "Indian Drainage System"
    },
    "General Studies > Geography > World Drainage System": {
        "subject": "General Studies",
        "topic": "Geography",
        "subtopic": "World Drainage System"
    },
    "General Studies > Geography > Minerals and Energy Resources in India": {
        "subject": "General Studies",
        "topic": "Geography",
        "subtopic": "Minerals and Energy Resources in India"
    },
    "General Studies > Geography > Agriculture": {
        "subject": "General Studies",
        "topic": "Geography",
        "subtopic": "Agriculture"
    },
    "General Studies > Geography > Soil": {
        "subject": "General Studies",
        "topic": "Geography",
        "subtopic": "Soil"
    },
    "General Studies > Geography > Crops": {
        "subject": "General Studies",
        "topic": "Geography",
        "subtopic": "Crops"
    },
    "General Studies > Geography > Vegetation": {
        "subject": "General Studies",
        "topic": "Geography",
        "subtopic": "Vegetation"
    },
    "General Studies > Geography > Climate": {
        "subject": "General Studies",
        "topic": "Geography",
        "subtopic": "Climate"
    },
    "General Studies > Geography > Industries": {
        "subject": "General Studies",
        "topic": "Geography",
        "subtopic": "Industries"
    },
    "General Studies > Geography > NAP/WLS/Biosphere Reserves/Various Initiatives": {
        "subject": "General Studies",
        "topic": "Geography",
        "subtopic": "NAP/WLS/Biosphere Reserves/Various Initiatives"
    },
    "General Studies > Geography > Physiographic Division of India": {
        "subject": "General Studies",
        "topic": "Geography",
        "subtopic": "Physiographic Division of India"
    },
    "General Studies > Geography > Transportation": {
        "subject": "General Studies",
        "topic": "Geography",
        "subtopic": "Transportation"
    },
    "General Studies > Geography > Population": {
        "subject": "General Studies",
        "topic": "Geography",
        "subtopic": "Population"
    },
    "General Studies > Geography > Atmosphere": {
        "subject": "General Studies",
        "topic": "Geography",
        "subtopic": "Atmosphere"
    },
    "General Studies > Geography > Rocks": {
        "subject": "General Studies",
        "topic": "Geography",
        "subtopic": "Rocks"
    },
    "General Studies > Geography > Mountain": {
        "subject": "General Studies",
        "topic": "Geography",
        "subtopic": "Mountain"
    },
    "General Studies > Geography > Volcano": {
        "subject": "General Studies",
        "topic": "Geography",
        "subtopic": "Volcano"
    },
    "General Studies > Geography > World geography and Map": {
        "subject": "General Studies",
        "topic": "Geography",
        "subtopic": "World geography and Map"
    },
    "General Studies > Geography > Environment": {
        "subject": "General Studies",
        "topic": "Geography",
        "subtopic": "Environment"
    },
    "General Studies > Polity > Constitution": {
        "subject": "General Studies",
        "topic": "Polity",
        "subtopic": "Constitution"
    },
    "General Studies > Polity > Sources of Indian Constitution": {
        "subject": "General Studies",
        "topic": "Polity",
        "subtopic": "Sources of Indian Constitution"
    },
    "General Studies > Polity > Articles, Schedules, Parts and list": {
        "subject": "General Studies",
        "topic": "Polity",
        "subtopic": "Articles, Schedules, Parts and list"
    },
    "General Studies > Polity > Amendments": {
        "subject": "General Studies",
        "topic": "Polity",
        "subtopic": "Amendments"
    },
    "General Studies > Polity > DPSP": {
        "subject": "General Studies",
        "topic": "Polity",
        "subtopic": "DPSP"
    },
    "General Studies > Polity > Fundamental Rights and Duties": {
        "subject": "General Studies",
        "topic": "Polity",
        "subtopic": "Fundamental Rights and Duties"
    },
    "General Studies > Polity > Committee Reports": {
        "subject": "General Studies",
        "topic": "Polity",
        "subtopic": "Committee Reports"
    },
    "General Studies > Polity > Parliament": {
        "subject": "General Studies",
        "topic": "Polity",
        "subtopic": "Parliament"
    },
    "General Studies > Polity > President, Vice President and Prime Minister": {
        "subject": "General Studies",
        "topic": "Polity",
        "subtopic": "President, Vice President and Prime Minister"
    },
    "General Studies > Polity > Judiciary": {
        "subject": "General Studies",
        "topic": "Polity",
        "subtopic": "Judiciary"
    },
    "General Studies > Polity > Government Bodies": {
        "subject": "General Studies",
        "topic": "Polity",
        "subtopic": "Government Bodies"
    },
    "General Studies > Polity > Polity of neighbouring countries": {
        "subject": "General Studies",
        "topic": "Polity",
        "subtopic": "Polity of neighbouring countries"
    },
    "General Studies > Polity > Important Cases": {
        "subject": "General Studies",
        "topic": "Polity",
        "subtopic": "Important Cases"
    },
    "General Studies > Economy > Basics of Economy": {
        "subject": "General Studies",
        "topic": "Economy",
        "subtopic": "Basics of Economy"
    },
    "General Studies > Economy > Concepts of Demand and Supply": {
        "subject": "General Studies",
        "topic": "Economy",
        "subtopic": "Concepts of Demand and Supply"
    },
    "General Studies > Economy > Cost, Production, Consumption and Market": {
        "subject": "General Studies",
        "topic": "Economy",
        "subtopic": "Cost, Production, Consumption and Market"
    },
    "General Studies > Economy > National Income, Inflation, Budget,Taxation and GDP": {
        "subject": "General Studies",
        "topic": "Economy",
        "subtopic": "National Income, Inflation, Budget,Taxation and GDP"
    },
    "General Studies > Economy > Money Banking and Financial Institutions": {
        "subject": "General Studies",
        "topic": "Economy",
        "subtopic": "Money Banking and Financial Institutions"
    },
    "General Studies > Economy > Navratna / Maharatna / PSUs": {
        "subject": "General Studies",
        "topic": "Economy",
        "subtopic": "Navratna / Maharatna / PSUs"
    },
    "General Studies > Economy > International Organisations": {
        "subject": "General Studies",
        "topic": "Economy",
        "subtopic": "International Organisations"
    },
    "General Studies > Economy > Government Schemes": {
        "subject": "General Studies",
        "topic": "Economy",
        "subtopic": "Government Schemes"
    },
    "General Studies > Economy > Five - Year Plans": {
        "subject": "General Studies",
        "topic": "Economy",
        "subtopic": "Five - Year Plans"
    },
    "General Studies > Economy > LPG": {
        "subject": "General Studies",
        "topic": "Economy",
        "subtopic": "LPG"
    },
    "General Studies > Economy > Indian Economy : Central Problems and Planning": {
        "subject": "General Studies",
        "topic": "Economy",
        "subtopic": "Indian Economy : Central Problems and Planning"
    },
    "General Studies > Economy > Stock, Debentures and Foreign trade": {
        "subject": "General Studies",
        "topic": "Economy",
        "subtopic": "Stock, Debentures and Foreign trade"
    },
    "General Studies > Economy > Fiscal Policy and Monetary Policy": {
        "subject": "General Studies",
        "topic": "Economy",
        "subtopic": "Fiscal Policy and Monetary Policy"
    },
    "General Studies > Economy > Miscellaneous": {
        "subject": "General Studies",
        "topic": "Economy",
        "subtopic": "Miscellaneous"
    },
    "General Studies > Physics > Light and Optics": {
        "subject": "General Studies",
        "topic": "Physics",
        "subtopic": "Light and Optics"
    },
    "General Studies > Physics > Heat and Thermodynamics": {
        "subject": "General Studies",
        "topic": "Physics",
        "subtopic": "Heat and Thermodynamics"
    },
    "General Studies > Physics > Fluid Mechanics": {
        "subject": "General Studies",
        "topic": "Physics",
        "subtopic": "Fluid Mechanics"
    },
    "General Studies > Physics > Electric Current and Its Effects": {
        "subject": "General Studies",
        "topic": "Physics",
        "subtopic": "Electric Current and Its Effects"
    },
    "General Studies > Physics > Laws": {
        "subject": "General Studies",
        "topic": "Physics",
        "subtopic": "Laws"
    },
    "General Studies > Physics > Force and Pressure": {
        "subject": "General Studies",
        "topic": "Physics",
        "subtopic": "Force and Pressure"
    },
    "General Studies > Physics > Sound": {
        "subject": "General Studies",
        "topic": "Physics",
        "subtopic": "Sound"
    },
    "General Studies > Physics > Gravitation": {
        "subject": "General Studies",
        "topic": "Physics",
        "subtopic": "Gravitation"
    },
    "General Studies > Physics > Work and Energy": {
        "subject": "General Studies",
        "topic": "Physics",
        "subtopic": "Work and Energy"
    },
    "General Studies > Physics > Wave": {
        "subject": "General Studies",
        "topic": "Physics",
        "subtopic": "Wave"
    },
    "General Studies > Physics > Radioactivity": {
        "subject": "General Studies",
        "topic": "Physics",
        "subtopic": "Radioactivity"
    },
    "General Studies > Physics > Discoveries": {
        "subject": "General Studies",
        "topic": "Physics",
        "subtopic": "Discoveries"
    },
    "General Studies > Physics > Units and Measurements": {
        "subject": "General Studies",
        "topic": "Physics",
        "subtopic": "Units and Measurements"
    },
    "General Studies > Physics > Miscellaneous": {
        "subject": "General Studies",
        "topic": "Physics",
        "subtopic": "Miscellaneous"
    },
    "General Studies > Chemistry > Structure of Atom": {
        "subject": "General Studies",
        "topic": "Chemistry",
        "subtopic": "Structure of Atom"
    },
    "General Studies > Chemistry > Compounds": {
        "subject": "General Studies",
        "topic": "Chemistry",
        "subtopic": "Compounds"
    },
    "General Studies > Chemistry > Metals, Non-metals and Alloys": {
        "subject": "General Studies",
        "topic": "Chemistry",
        "subtopic": "Metals, Non-metals and Alloys"
    },
    "General Studies > Chemistry > Acid, Bases and Salt": {
        "subject": "General Studies",
        "topic": "Chemistry",
        "subtopic": "Acid, Bases and Salt"
    },
    "General Studies > Chemistry > Metallurgy": {
        "subject": "General Studies",
        "topic": "Chemistry",
        "subtopic": "Metallurgy"
    },
    "General Studies > Chemistry > Organic Chemistry": {
        "subject": "General Studies",
        "topic": "Chemistry",
        "subtopic": "Organic Chemistry"
    },
    "General Studies > Chemistry > Periodic table": {
        "subject": "General Studies",
        "topic": "Chemistry",
        "subtopic": "Periodic table"
    },
    "General Studies > Chemistry > Ideal Gas Law": {
        "subject": "General Studies",
        "topic": "Chemistry",
        "subtopic": "Ideal Gas Law"
    },
    "General Studies > Chemistry > Chemical Properties": {
        "subject": "General Studies",
        "topic": "Chemistry",
        "subtopic": "Chemical Properties"
    },
    "General Studies > Chemistry > Solutions": {
        "subject": "General Studies",
        "topic": "Chemistry",
        "subtopic": "Solutions"
    },
    "General Studies > Chemistry > Chemistry in Everyday life": {
        "subject": "General Studies",
        "topic": "Chemistry",
        "subtopic": "Chemistry in Everyday life"
    },
    "General Studies > Chemistry > Discoveries": {
        "subject": "General Studies",
        "topic": "Chemistry",
        "subtopic": "Discoveries"
    },
    "General Studies > Chemistry > Common Names": {
        "subject": "General Studies",
        "topic": "Chemistry",
        "subtopic": "Common Names"
    },
    "General Studies > Chemistry > Miscellaneous": {
        "subject": "General Studies",
        "topic": "Chemistry",
        "subtopic": "Miscellaneous"
    },
    "General Studies > Biology > Scientific Names": {
        "subject": "General Studies",
        "topic": "Biology",
        "subtopic": "Scientific Names"
    },
    "General Studies > Biology > Nutrition in Animals": {
        "subject": "General Studies",
        "topic": "Biology",
        "subtopic": "Nutrition in Animals"
    },
    "General Studies > Biology > Nutrition in plants": {
        "subject": "General Studies",
        "topic": "Biology",
        "subtopic": "Nutrition in plants"
    },
    "General Studies > Biology > Deficiency and Diseases": {
        "subject": "General Studies",
        "topic": "Biology",
        "subtopic": "Deficiency and Diseases"
    },
    "General Studies > Biology > Reproduction in Animals": {
        "subject": "General Studies",
        "topic": "Biology",
        "subtopic": "Reproduction in Animals"
    },
    "General Studies > Biology > Reproduction in Plants": {
        "subject": "General Studies",
        "topic": "Biology",
        "subtopic": "Reproduction in Plants"
    },
    "General Studies > Biology > Cell: Basic Unit of life": {
        "subject": "General Studies",
        "topic": "Biology",
        "subtopic": "Cell: Basic Unit of life"
    },
    "General Studies > Biology > Sensory Organs": {
        "subject": "General Studies",
        "topic": "Biology",
        "subtopic": "Sensory Organs"
    },
    "General Studies > Biology > Circulatory System": {
        "subject": "General Studies",
        "topic": "Biology",
        "subtopic": "Circulatory System"
    },
    "General Studies > Biology > Excretory System": {
        "subject": "General Studies",
        "topic": "Biology",
        "subtopic": "Excretory System"
    },
    "General Studies > Biology > Endocrine/Exocrine system": {
        "subject": "General Studies",
        "topic": "Biology",
        "subtopic": "Endocrine/Exocrine system"
    },
    "General Studies > Biology > Respiratory system": {
        "subject": "General Studies",
        "topic": "Biology",
        "subtopic": "Respiratory system"
    },
    "General Studies > Biology > Digestive system": {
        "subject": "General Studies",
        "topic": "Biology",
        "subtopic": "Digestive system"
    },
    "General Studies > Biology > Nervous system": {
        "subject": "General Studies",
        "topic": "Biology",
        "subtopic": "Nervous system"
    },
    "General Studies > Biology > Skeleton system": {
        "subject": "General Studies",
        "topic": "Biology",
        "subtopic": "Skeleton system"
    },
    "General Studies > Biology > Plant Kingdom": {
        "subject": "General Studies",
        "topic": "Biology",
        "subtopic": "Plant Kingdom"
    },
    "General Studies > Biology > Animal Kingdom": {
        "subject": "General Studies",
        "topic": "Biology",
        "subtopic": "Animal Kingdom"
    },
    "General Studies > Biology > Micro organisms": {
        "subject": "General Studies",
        "topic": "Biology",
        "subtopic": "Micro organisms"
    },
    "General Studies > Biology > Enzymes and Hormones": {
        "subject": "General Studies",
        "topic": "Biology",
        "subtopic": "Enzymes and Hormones"
    },
    "General Studies > Biology > Discoveries and vaccines": {
        "subject": "General Studies",
        "topic": "Biology",
        "subtopic": "Discoveries and vaccines"
    },
    "General Studies > Biology > Scientific Study": {
        "subject": "General Studies",
        "topic": "Biology",
        "subtopic": "Scientific Study"
    },
    "General Studies > Biology > Miscellaneous": {
        "subject": "General Studies",
        "topic": "Biology",
        "subtopic": "Miscellaneous"
    },
    "Static GK > Static GK > Important Days": {
        "subject": "Static GK",
        "topic": "Static GK",
        "subtopic": "Important Days"
    },
    "Static GK > Static GK > Appointments": {
        "subject": "Static GK",
        "topic": "Static GK",
        "subtopic": "Appointments"
    },
    "Static GK > Static GK > Places": {
        "subject": "Static GK",
        "topic": "Static GK",
        "subtopic": "Places"
    },
    "Static GK > Static GK > Arts Personality": {
        "subject": "Static GK",
        "topic": "Static GK",
        "subtopic": "Arts Personality"
    },
    "Static GK > Static GK > Head Quaters": {
        "subject": "Static GK",
        "topic": "Static GK",
        "subtopic": "Head Quaters"
    },
    "Static GK > Static GK > Arts Awards": {
        "subject": "Static GK",
        "topic": "Static GK",
        "subtopic": "Arts Awards"
    },
    "Static GK > Static GK > Musical Instruments": {
        "subject": "Static GK",
        "topic": "Static GK",
        "subtopic": "Musical Instruments"
    },
    "Static GK > Static GK > Festivals": {
        "subject": "Static GK",
        "topic": "Static GK",
        "subtopic": "Festivals"
    },
    "Static GK > Static GK > Dances": {
        "subject": "Static GK",
        "topic": "Static GK",
        "subtopic": "Dances"
    },
    "Static GK > Static GK > Fairs": {
        "subject": "Static GK",
        "topic": "Static GK",
        "subtopic": "Fairs"
    },
    "Static GK > Static GK > Songs": {
        "subject": "Static GK",
        "topic": "Static GK",
        "subtopic": "Songs"
    },
    "Static GK > Static GK > Painting/Dress/Tribes": {
        "subject": "Static GK",
        "topic": "Static GK",
        "subtopic": "Painting/Dress/Tribes"
    },
    "Static GK > Static GK > First in India/World": {
        "subject": "Static GK",
        "topic": "Static GK",
        "subtopic": "First in India/World"
    },
    "Static GK > Static GK > Sports": {
        "subject": "Static GK",
        "topic": "Static GK",
        "subtopic": "Sports"
    },
    "Static GK > Static GK > Books and Authors": {
        "subject": "Static GK",
        "topic": "Static GK",
        "subtopic": "Books and Authors"
    },
    "Static GK > Static GK > Famous Personalities": {
        "subject": "Static GK",
        "topic": "Static GK",
        "subtopic": "Famous Personalities"
    },
    "Static GK > Static GK > States G.K.": {
        "subject": "Static GK",
        "topic": "Static GK",
        "subtopic": "States G.K."
    },
    "Static GK > Static GK > Organisations": {
        "subject": "Static GK",
        "topic": "Static GK",
        "subtopic": "Organisations"
    },
    "Static GK > Static GK > World G.K": {
        "subject": "Static GK",
        "topic": "Static GK",
        "subtopic": "World G.K"
    },
    "Static GK > Static GK > Full forms": {
        "subject": "Static GK",
        "topic": "Static GK",
        "subtopic": "Full forms"
    },
    "Static GK > Static GK > Religious Places": {
        "subject": "Static GK",
        "topic": "Static GK",
        "subtopic": "Religious Places"
    },
    "Static GK > Static GK > Awards": {
        "subject": "Static GK",
        "topic": "Static GK",
        "subtopic": "Awards"
    },
    "Static GK > Static GK > Important Events": {
        "subject": "Static GK",
        "topic": "Static GK",
        "subtopic": "Important Events"
    },
    "Static GK > Static GK > Founders": {
        "subject": "Static GK",
        "topic": "Static GK",
        "subtopic": "Founders"
    },
    "Static GK > Static GK > Schemes": {
        "subject": "Static GK",
        "topic": "Static GK",
        "subtopic": "Schemes"
    },
    "Static GK > Static GK > Discoveries": {
        "subject": "Static GK",
        "topic": "Static GK",
        "subtopic": "Discoveries"
    },
    "Static GK > Static GK > IUCN Red Lisst": {
        "subject": "Static GK",
        "topic": "Static GK",
        "subtopic": "IUCN Red Lisst"
    },
    "Static GK > Static GK > Themes": {
        "subject": "Static GK",
        "topic": "Static GK",
        "subtopic": "Themes"
    },
    "Static GK > Static GK > Miscellaneous": {
        "subject": "Static GK",
        "topic": "Static GK",
        "subtopic": "Miscellaneous"
    },
    "Computer Awareness > Computer Basics > Organization of a computer": {
        "subject": "Computer Awareness",
        "topic": "Computer Basics",
        "subtopic": "Organization of a computer"
    },
    "Computer Awareness > Computer Basics > Central Processing Unit (CPU)": {
        "subject": "Computer Awareness",
        "topic": "Computer Basics",
        "subtopic": "Central Processing Unit (CPU)"
    },
    "Computer Awareness > Computer Basics > Input/Output devices": {
        "subject": "Computer Awareness",
        "topic": "Computer Basics",
        "subtopic": "Input/Output devices"
    },
    "Computer Awareness > Computer Basics > Computer memory": {
        "subject": "Computer Awareness",
        "topic": "Computer Basics",
        "subtopic": "Computer memory"
    },
    "Computer Awareness > Computer Basics > Memory organization": {
        "subject": "Computer Awareness",
        "topic": "Computer Basics",
        "subtopic": "Memory organization"
    },
    "Computer Awareness > Computer Basics > Backup devices": {
        "subject": "Computer Awareness",
        "topic": "Computer Basics",
        "subtopic": "Backup devices"
    },
    "Computer Awareness > Computer Basics > PORTs": {
        "subject": "Computer Awareness",
        "topic": "Computer Basics",
        "subtopic": "PORTs"
    },
    "Computer Awareness > Computer Basics > Windows Explorer": {
        "subject": "Computer Awareness",
        "topic": "Computer Basics",
        "subtopic": "Windows Explorer"
    },
    "Computer Awareness > Computer Basics > Keyboard shortcuts": {
        "subject": "Computer Awareness",
        "topic": "Computer Basics",
        "subtopic": "Keyboard shortcuts"
    },
    "Computer Awareness > Software > Windows Operating System": {
        "subject": "Computer Awareness",
        "topic": "Software",
        "subtopic": "Windows Operating System"
    },
    "Computer Awareness > Software > Basics of Microsoft Office (MS Word, MS Excel, PowerPoint)": {
        "subject": "Computer Awareness",
        "topic": "Software",
        "subtopic": "Basics of Microsoft Office (MS Word, MS Excel, PowerPoint)"
    },
    "Computer Awareness > Working with Internet and E-mails > Web Browsing & Searching": {
        "subject": "Computer Awareness",
        "topic": "Working with Internet and E-mails",
        "subtopic": "Web Browsing & Searching"
    },
    "Computer Awareness > Working with Internet and E-mails > Downloading & Uploading": {
        "subject": "Computer Awareness",
        "topic": "Working with Internet and E-mails",
        "subtopic": "Downloading & Uploading"
    },
    "Computer Awareness > Working with Internet and E-mails > Managing an E-mail Account": {
        "subject": "Computer Awareness",
        "topic": "Working with Internet and E-mails",
        "subtopic": "Managing an E-mail Account"
    },
    "Computer Awareness > Working with Internet and E-mails > e-Banking": {
        "subject": "Computer Awareness",
        "topic": "Working with Internet and E-mails",
        "subtopic": "e-Banking"
    },
    "Computer Awareness > Networking and Cyber Security > Networking devices and protocols": {
        "subject": "Computer Awareness",
        "topic": "Networking and Cyber Security",
        "subtopic": "Networking devices and protocols"
    },
    "Computer Awareness > Networking and Cyber Security > Network and information security threats (hacking, virus, worms, Trojan, etc.)": {
        "subject": "Computer Awareness",
        "topic": "Networking and Cyber Security",
        "subtopic": "Network and information security threats (hacking, virus, worms, Trojan, etc.)"
    },
    "Computer Awareness > Networking and Cyber Security > Preventive measures": {
        "subject": "Computer Awareness",
        "topic": "Networking and Cyber Security",
        "subtopic": "Preventive measures"
    },
}


# ===== SUMMARY STATISTICS =====
TAXONOMY_STATS = {
    "TNPSC": 623,
    "BANKING": 232,
    "SSC_RAILWAYS": 669,
}

TOTAL_TRIPLETS = 1524

# ===== HELPER FUNCTIONS =====
def get_taxonomy_for_exam(exam_type: str):
    """Get taxonomy constants for a specific exam type"""
    exam_map = {
        "TNPSC": {
            "subjects": TNPSC_SUBJECTS,
            "triplets": TNPSC_TRIPLETS,
            "triplet_dict": TNPSC_TRIPLET_DICT
        },
        "Banking": {
            "subjects": BANKING_SUBJECTS,
            "triplets": BANKING_TRIPLETS,
            "triplet_dict": BANKING_TRIPLET_DICT
        },
        "SSC-Railways": {
            "subjects": SSC_RAILWAYS_SUBJECTS,
            "triplets": SSC_RAILWAYS_TRIPLETS,
            "triplet_dict": SSC_RAILWAYS_TRIPLET_DICT
        }
    }
    return exam_map.get(exam_type)
