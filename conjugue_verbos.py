def normalize_prefix(prefix, replacements):
    for replacement in replacements:
        if prefix.endswith(replacement['ifIs']):
            prefix = prefix[:-len(replacement['ifIs'])] + \
                replacement['replaceBy']
    return prefix


def build_ar(prefix):
    conjugado = {
        "present_tense": [
            prefix + 'o',
            prefix + 'as',
            prefix + 'a',
            prefix + 'amos',
            prefix + 'ais',
            prefix + 'am'
        ],
        "imperfect_past_tense": [
            prefix + 'ava',
            prefix + 'avas',
            prefix + 'ava',
            prefix + 'ávamos',
            prefix + 'áveis',
            prefix + 'avam'
        ],
        "preterito_perfeito": [
            normalize_prefix(prefix, [
                {
                    'ifIs': 'ç',
                    'replaceBy': 'c'
                },
                {
                    'ifIs': 'c',
                    'replaceBy': 'qu'
                },
                {
                    'ifIs': 'g',
                    'replaceBy': 'gu'
                },
            ]) + 'ei',
        ],
        "preterito_mais_que_perfeito": [
            prefix + 'ara',
            prefix + 'aras',
            prefix + 'ara',
            prefix + 'áramos',
            prefix + 'áreis',
            prefix + 'aram'
        ],
        # fpte = [
        "future_simple_tense": [
            prefix + 'arei',
            prefix + 'arás',
            prefix + 'ará',
            prefix + 'aremos',
            prefix + 'areis',
            prefix + 'arão'
        ],
        # fpto = (
        "conditional_mood": [
            prefix + 'aria',
            prefix + 'arias',
            prefix + 'aria',
            prefix + 'aríamos',
            prefix + 'aríeis',
            prefix + 'ariam'
        ]
    }
    return conjugado


def build_er(prefix):

    if prefix.endswith('ser'):
        conjugado = {
            "presente": [
                "sou",
                "és",
                "é",
                "somos",
                "sois",
                "são"
            ],
            "pretérito_imperfeito": [
                "era",
                "eras",
                "era",
                "éramos",
                "éreis",
                "eram"
            ],
            "pretérito_perfeito": [
                "fui",
                "foste",
                "foi",
                "fomos",
                "fostes",
                "foram"
            ],
            "pretérito_mais_que_perfeito": [
                "fora",
                "foras",
                "fora",
                "fôramos",
                "fôreis",
                "foram"
            ],
            "futuro_do_presente": [
                "serei",
                "serás",
                "será",
                "seremos",
                "sereis",
                "serão"
            ],
            "futuro_do_pretérito": [
                "seria",
                "serias",
                "seria",
                "seríamos",
                "seríeis",
                "seriam"
            ]
        }
        return conjugado
    elif prefix.endswith('saber'):
        conjugado = {
            "presente": [
                "sei",
                "sabes",
                "sabe",
                "sabemos",
                "sabeis",
                "sabem"
            ],
            "pretérito_imperfeito": [
                "sabia",
                "sabias",
                "sabia",
                "sabíamos",
                "sabíeis",
                "sabiam"
            ],
            "pretérito_perfeito": [
                "soube",
                "soubeste",
                "soube",
                "soubemos",
                "soubestes",
                "souberam"
            ],
            "pretérito_mais_que_perfeito": [
                "soubera",
                "souberas",
                "soubera",
                "soubéramos",
                "soubéreis",
                "souberam"
            ],
            "futuro_do_presente": [
                "saberei",
                "saberás",
                "saberá",
                "saberemos",
                "sabereis",
                "saberão"
            ],
            "futuro_do_pretérito": [
                "saberia",
                "saberias",
                "saberia",
                "saberíamos",
                "saberíeis",
                "saberiam"
            ]
        }
        return conjugado
    else:
        conjugado = {
            "present_tense": [
                normalize_prefix(prefix, [
                    {
                        'ifIs': 'c',
                        'replaceBy': 'ç'
                    }
                ]) + 'o',
                prefix + 'es',
                prefix + 'e',
                prefix + 'emos',
                prefix + 'eis',
                prefix + 'em'
            ],
            "imperfect_past_tense": [
                prefix + 'ia',
                prefix + 'ias',
                prefix + 'ia',
                prefix + 'íamos',
                prefix + 'íeis',
                prefix + 'iam'
            ],
            "preterite_perfect_tense": [
                prefix + 'i',
                prefix + 'este',
                prefix + 'eu',
                prefix + 'emos',
                prefix + 'estes',
                prefix + 'eram'
            ],
            "pluperfect_mood": [
                prefix + 'era',
                prefix + 'eras',
                prefix + 'era',
                prefix + 'êramos',
                prefix + 'êreis',
                prefix + 'eram'
            ],
            # fpte = [
            "future_simple_tense": [
                prefix + 'erei',
                prefix + 'erás',
                prefix + 'erá',
                prefix + 'eremos',
                prefix + 'ereis',
                prefix + 'erão'
            ],
            # fpto = (
            "conditional_mood": [
                prefix + 'eria',
                prefix + 'erias',
                prefix + 'eria',
                prefix + 'eríamos',
                prefix + 'eríeis',
                prefix + 'eriam'
            ]
        }
        return conjugado


def build_ir(prefix):
    conjugado = {
        "present_tense": [
            prefix + 'o',
            prefix + 'es',
            prefix + 'e',
            prefix + 'imos',
            prefix + 'is',
            prefix + 'em'
        ],
        "imperfect_past_tense": [
            prefix + 'ia',
            prefix + 'ias',
            prefix + 'ia',
            prefix + 'íamos',
            prefix + 'íeis',
            prefix + 'iam'
        ],
        "preterite_perfect_tense": [
            prefix + 'i',
            prefix + 'este',
            prefix + 'eu',
            prefix + 'emos',
            prefix + 'estes',
            prefix + 'eram'
        ],
        "pluperfect_mood": [
            prefix + 'i',
            prefix + 'iste',
            prefix + 'iu',
            prefix + 'imos',
            prefix + 'istes',
            prefix + 'iram'
        ],
        "future_simple_tense": [
            prefix + 'irei',
            prefix + 'irás',
            prefix + 'irá',
            prefix + 'iremos',
            prefix + 'ireis',
            prefix + 'irão'
        ],
        "conditional_mood": [
            prefix + 'iria',
            prefix + 'irias',
            prefix + 'iria',
            prefix + 'iríamos',
            prefix + 'iríeis',
            prefix + 'iriam'
        ]
    }
    return conjugado


def build_por(prefix):
    conjugado = {
        "present_tense": [
            prefix + 'onho',
            prefix + 'ões',
            prefix + 'õe',
            prefix + 'omos',
            prefix + 'ondes',
            prefix + 'õem'
        ],
        "imperfect_past_tense": [
            prefix + 'unha',
            prefix + 'unhas',
            prefix + 'unha',
            prefix + 'únhamos',
            prefix + 'únheis',
            prefix + 'unham'
        ],
        "preterite_perfect_tense": [
            prefix + 'us',
            prefix + 'useste',
            prefix + 'ôs',
            prefix + 'usemos',
            prefix + 'usestes',
            prefix + 'useram'
        ],
        "pluperfect_mood": [
            prefix + 'usera',
            prefix + 'useras',
            prefix + 'usera',
            prefix + 'uséramos',
            prefix + 'uséreis',
            prefix + 'useram'
        ],
        "future_simple_tense": [
            prefix + 'orei',
            prefix + 'orás',
            prefix + 'orá',
            prefix + 'oremos',
            prefix + 'oreis',
            prefix + 'orão'
        ],
        "conditional_mood": [
            prefix + 'oria',
            prefix + 'orias',
            prefix + 'oria',
            prefix + 'oríamos',
            prefix + 'oríeis',
            prefix + 'oriam'
        ]
    }
    return conjugado

# Eu
# Tu
# Ele/ela
# Nós
# Vós
# Eles/elas

def tip_verb(verb):
    if verb.endswith('ar'):
        return build_ar(verb[:-2])
    elif verb.endswith('er'):
        return build_er(verb[:-2])
    elif verb.endswith('ir'):
        return build_ir(verb[:-2])
    elif verb.endswith('or'):
        return build_por(verb[:-2])
    else:
        print("Desconhecido")


print(tip_verb('nascer'))
# Ser: sou, és, é, somos, sois, são
# Ir: vou, vais, vai, vamos, ides, vão
# Ter: tenho, tens, tem, temos, tendes, têm
# Fazer: faço, fazes, faz, fazemos, fazeis, fazem
# Ver: vejo, vês, vê, vemos, vedes, veem
# Estar: estou, estás, está, estamos, estais, estão
# Dar: dou, dás, dá, damos, dais, dão
# Saber: sei, sabes, sabe, sabemos, sabeis, sabem
# Querer: quero, queres, quer, queremos, quereis, querem
# Poder: posso, podes, pode, podemos, podeis, podem