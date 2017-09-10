import random

from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from apps.messenger.components.attachments import TemplateAttachment, VideoAttachment
from apps.messenger.components.buttons import PostbackButton, LoginButton, URLButton
from apps.messenger.components.elements import ListElement, Element, ReceiptElement, ReceiptAddress, Summary, \
    Adjustment
from apps.messenger.components.messages import Message
from apps.messenger.components.requests import MessageRequest
from apps.messenger.components.templates import ListTemplate, GenericTemplate, ReceiptTemplate
from apps.messenger.components.replies import QuickReplies, TextReply, LocationReply
from apps.messenger.motos import constants
from apps.messenger.samples.responses import Components

from apps.producto.models import Producto
from apps.repuesto.models import Repuesto
from apps.propaganda.models import Propaganda
from apps.reparacion.models import Asistencia

class RepliesMixin(object):

    def __init__(self, event, messenger):
        self.event = event
        self.messenger =  messenger

    def typing(self):
        responses = list()
        responses.append(MessageRequest(self.event.sender, sender_action='mark_seen'))
        responses.append(MessageRequest(self.event.sender, sender_action='typing_on'))
        self.messenger.post_message_queue(responses)
        

    def render_start(self):

        self.typing()
        responses = list()
        message = Message(text="Que deseas hacer?")
        responses.append(MessageRequest(self.event.sender, message))

        template = ListTemplate(
            elements=[
                ListElement(
                    title="ASISTENCIA",
                    image_url="https://goo.gl/C9hHzy",
                    subtitle="Asistencia Mecanica",
                    buttons=[
                        PostbackButton(
                            title="Consultar",
                            payload=constants.SHOW_REPARACION
                        )
                    ],
                ),
                ListElement(
                    title="USMOTOS",
                    image_url="https://goo.gl/5EGLWp",
                    subtitle="usmotos",
                    buttons=[
                        PostbackButton(
                            title="Conocer",
                            payload=constants.INFORMATION_BUSINESS
                        )
                    ],
                ),
                ListElement(
                    title="PRODUCTOS",
                    image_url="https://goo.gl/wFPqYL",
                    subtitle="Motocicletas y Accesorios",
                    buttons=[
                        PostbackButton(
                            title="Ver",
                            payload=constants.SHOW_PRODUCTS
                        )
                    ],
                ),
                ListElement(
                    title="AYUDA",
                    image_url="https://goo.gl/JUHMtP",
                    subtitle="Necesitas Ayuda?",
                    buttons=[
                        PostbackButton(
                            title="Ayuda",
                            payload=constants.SHOW_INFO
                        )
                    ],
                )
            ]
        )
        attachment = TemplateAttachment(template=template)
        message = Message(attachment=attachment)
        responses.append(Components.typing(responses, self.event.sender))
        responses.append(MessageRequest(self.event.sender, message))
        self.messenger.post_message_queue(responses)


    def render_products(self):
        self.typing()
        responses = list()
        replies = QuickReplies(
            replies=[
                TextReply(
                    image_url="https://goo.gl/wFPqYL",
                    title="MOTOCICLETAS",
                    payload=constants.SHOW_CATEGORY_MOTORCYCLE,
                ),

                TextReply(
                    image_url="https://goo.gl/6FqKDQ",
                    title="ACCESORIOS",
                    payload=constants.SHOW_ACCESORIES,
                ),

                TextReply(
                    image_url="https://goo.gl/gY5Kr9",
                    title="PROMOCIONES",
                    payload=constants.SHOW_PROMOTIONS,
                ),
                # LocationReply(), PARA LAS DIRECCIONES

                TextReply(
                    image_url="https://goo.gl/oY50Tk",
                    title="CANCELAR",
                    payload=constants.CANCEL,
                ),
            ]
        )
        message = Message(
            text="¿que seleccionaras 😄?",
            quick_replies=replies
        )
        responses.append(MessageRequest(self.event.sender, message))
        self.messenger.post_message_queue(responses)

    def render_show_information(self):
        self.typing()
        responses = list()
        replies = QuickReplies(
            replies=[
                TextReply(
                    image_url="https://goo.gl/KKzi8q",
                    title="MISION",
                    payload=constants.MISSION,
                ),

                TextReply(
                    image_url="https://goo.gl/KKzi8q",
                    title="VISION",
                    payload=constants.VIEW,
                ),

                TextReply(
                    image_url="https://goo.gl/KKzi8q",
                    title="HORARIOS",
                    payload=constants.SCHEDULE,
                ),

                TextReply(
                    image_url="https://goo.gl/KKzi8q",
                    title="DIRECCION",
                    payload=constants.ADDRESS,
                ),


                TextReply(
                    image_url="https://goo.gl/oY50Tk",
                    title="CANCELAR",
                    payload=constants.START,
                ),
            ]
        )
        message = Message(
            text="Aqui tienes informacion de la empresa 😄",
            quick_replies=replies
        )
        responses.append(MessageRequest(self.event.sender, message))
        self.messenger.post_message_queue(responses)

    def render_show_view(self):
        self.typing()
        responses = list()
        replies = QuickReplies(
            replies=[

                TextReply(
                    image_url="https://goo.gl/KKzi8q",
                    title="REGRESA",
                    payload=constants.INFORMATION_BUSINESS,
                ),

                TextReply(
                    image_url="https://goo.gl/oY50Tk",
                    title="INICIO",
                    payload=constants.START,
                ),
            ]
        )

        message = Message(
            text="⭐ Empresa dedicada a ala distribucion y comercializacion de Motocicletas\n"
                 "Apoyados por un equipo 🙂 calificado con actitud de servicio y honestidad 🔧 👍.",
            quick_replies=replies
            )

        responses.append(MessageRequest(self.event.sender, message))
        self.messenger.post_message_queue(responses)


    def render_show_mission(self):
        self.typing()
        responses = list()
        replies = QuickReplies(
            replies=[

                TextReply(
                    image_url="https://goo.gl/KKzi8q",
                    title="REGRESA",
                    payload=constants.INFORMATION_BUSINESS,
                ),

                TextReply(
                    image_url="https://goo.gl/oY50Tk",
                    title="INICIO",
                    payload=constants.START,
                ),
            ]
        )
        message = Message(
            text="😀 En el 2020 ser reconocido como empresa lider a nivel nacional 💡 ✅ en distribucion de Motocicletas\n"
                 "por la calidad y amplio portafolio y productos y servicios que ofrece.",
            quick_replies=replies
            )
        responses.append(MessageRequest(self.event.sender, message))
        self.messenger.post_message_queue(responses)


    def render_show_address(self):
        self.typing()
        responses = list()
        replies = QuickReplies(
            replies=[

                TextReply(
                    image_url="https://goo.gl/KKzi8q",
                    title="REGRESA",
                    payload=constants.INFORMATION_BUSINESS,
                ),

                TextReply(
                    image_url="https://goo.gl/oY50Tk",
                    title="INICIO",
                    payload=constants.START,
                ),
            ]
        )
        message = Message(
            text="👉 c. Panamá esq. Brasil # 1590, La Paz, Bolivia 😎\n"
                 "📞 2115625 📱",
            quick_replies = replies
            )
        responses.append(MessageRequest(self.event.sender, message))
        self.messenger.post_message_queue(responses)

    def render_show_schedule(self):
        self.typing()
        responses = list()
        replies = QuickReplies(
            replies=[

                TextReply(
                    image_url="https://goo.gl/KKzi8q",
                    title="REGRESA",
                    payload=constants.INFORMATION_BUSINESS,
                ),

                TextReply(
                    image_url="https://goo.gl/oY50Tk",
                    title="INICIO",
                    payload=constants.START,
                ),
            ]
        )
        message = Message(
            text="⌚ Abre a las 8:30 (8:30 - 12:30, 14:30 - 19:00) 🌞",
            quick_replies = replies
            )
        responses.append(MessageRequest(self.event.sender, message))
        self.messenger.post_message_queue(responses)


    def render_categorys_moto(self):
        elements = []

        # ("NAKED", 'naked'),
        # ("SCOOTER", 'scooter'),
        # ("CRUCERO", 'crucero'),
        # ("CHOOPER", 'chooper'),
        # ("CUSTOM", 'custom'),
        # ("SIDECAR", 'sidecar'),
        # ("TOURING", 'touring'),
        # ("RACER", 'racer'),
        # ("TRIAL", 'trial'),

        self.typing()
        responses = list()

        text = TextReply(
                    title="NAKED",
                    image_url='https://goo.gl/62juy0',
                    payload=constants.NAKED,
                )
        elements.append(text)

        text = TextReply(
                    title="SCOOTER",
                    image_url='https://goo.gl/hrU5Uu',
                    payload=constants.SCOOTER,
                )
        elements.append(text)

        text = TextReply(
                    title="CRUCERO",
                    image_url='https://goo.gl/oYUSxA',
                    payload=constants.CRUCERO,
                )
        elements.append(text)

        text = TextReply(
                    title="CHOOPER",
                    image_url='https://goo.gl/HsG2Zu',
                    payload=constants.CHOOPER,
                )
        elements.append(text)

        text = TextReply(
                    title="CUSTOM",
                    image_url='https://goo.gl/WMAjzN',
                    payload=constants.CUSTOM,
                )
        elements.append(text)

        text = TextReply(
                    title="SIDECAR",
                    image_url='https://goo.gl/0YYM0c',
                    payload=constants.SIDECAR,
                )
        elements.append(text)

        text = TextReply(
                    title="TOURING",
                    image_url='https://goo.gl/dS0cqF',
                    payload=constants.TOURING,
                )
        elements.append(text)

        text = TextReply(
                    title="RACER",
                    image_url='https://goo.gl/PZz362',
                    payload=constants.RACER,
                )
        elements.append(text)

        text = TextReply(
                    title="TRIAL",
                    image_url='https://goo.gl/LXWy1a',
                    payload=constants.TRIAL,
                )
        elements.append(text)

        text = TextReply(
                    title="CANCELAR",
                    image_url="https://goo.gl/oY50Tk",
                    payload=constants.CANCEL,
                )
        elements.append(text)

        numbers = QuickReplies(
            replies=elements
        )

        message = Message(
            text="Categorias",
            quick_replies=numbers
        )

        responses.append(MessageRequest(self.event.sender, message))
        self.messenger.post_message_queue(responses)

    def render_show_moto_naked(self):
        self.typing()

        motos_naked = Producto.objects.all().filter(tipo = "Naked")

        _naked = 0

        for m_active in motos_naked:
            if m_active.habilitado == True and m_active.tipo == "Naked":
                _naked +=1 

        print("CANTIDAD NAKED", _naked)

        list_url_motos = [
            'https://goo.gl/GdgDbF',
            'https://goo.gl/opMbeu',
            'https://goo.gl/Q7799l',
            'https://goo.gl/y3Hym7',
            'https://goo.gl/09oGyc',
            'https://goo.gl/Q8UCXk',
            'https://goo.gl/knZMpb',
            'https://goo.gl/76utQ6',
            'https://goo.gl/SSvIoR',
            'https://goo.gl/KPfjnI',
            'https://goo.gl/X9PDCI',
            'https://goo.gl/vJwjcn',
            'https://goo.gl/CbGJWm',
            'https://goo.gl/PIbDBV',
            'https://goo.gl/Vd0BFC'
        ]

        responses = list()
        elements = []

        if _naked > 0 and _naked <= 10:
            message = Message(text="Aqui te muestro las motocicletas de Tipo Nacked", )
            responses.append(MessageRequest(self.event.sender, message))
            cont = 1

            for naked in motos_naked:
                if naked.cantidad > 0:
                    _venta = "DISPONIBLE"
                else:
                    _venta = "AGOTADO"

                if naked.habilitado == True:
                    element = Element(
                        title=naked.numero_serie,
                        image_url=list_url_motos[cont],
                        subtitle='{}-{}'.format(naked.color,_venta),
                        buttons=[
                            PostbackButton(
                                title="REGRESAR",
                                payload=constants.CATEGORYS_M
                            ),
                            PostbackButton(
                                title="INICIO",
                                payload=constants.START
                            ),
                        ]
                    )
                    elements.append(element)
                    cont += 1
            template = GenericTemplate(
                elements=elements
            )
            attachment = TemplateAttachment(template=template)
            message = Message(attachment=attachment)
            responses.append(Components.typing(responses, self.event.sender))
            responses.append(MessageRequest(self.event.sender, message))
        else:
            self.typing()
            responses = list()
            replies = QuickReplies(
                replies=[
                    TextReply(
                        image_url="https://goo.gl/Rg33Yq",
                        title="MENU INICIO",
                        payload=constants.START,
                    )
                ]
            )
            message = Message(
                text="Ups, 😱 lamentamos decirte que no hay motocicletas Naked registradas",
                quick_replies=replies
            )
            responses.append(MessageRequest(self.event.sender, message))
        self.messenger.post_message_queue(responses)



    def render_show_moto_scooter(self):
        self.typing()

        motos_scooter = Motorcycle.objects.all().filter(type = "SCOOTER")

        _scooter = 0

        for m_active in motos_scooter:
            if m_active.active == True and m_active.type == "SCOOTER":
                _scooter +=1 

        print("CANTIDAD SCOOTER", _scooter)

        list_url_motos = [
            'https://goo.gl/76utQ6',
            'https://goo.gl/SSvIoR',
            'https://goo.gl/KPfjnI',
            'https://goo.gl/X9PDCI',
            'https://goo.gl/vJwjcn',
            'https://goo.gl/CbGJWm',
            'https://goo.gl/PIbDBV',
            'https://goo.gl/Vd0BFC'
            'https://goo.gl/GdgDbF',
            'https://goo.gl/opMbeu',
            'https://goo.gl/Q7799l',
            'https://goo.gl/y3Hym7',
            'https://goo.gl/09oGyc',
            'https://goo.gl/Q8UCXk',
            'https://goo.gl/knZMpb'
        ]

        responses = list()
        elements = []

        if _scooter > 0 and _scooter <= 10:
            message = Message(text="Aqui te muestro las motocicletas de Tipo Scooter", )
            responses.append(MessageRequest(self.event.sender, message))
            cont = 1
            for scooter in motos_scooter:
                if scooter.stock > 0:
                    _venta = "DISPONIBLE"
                else:
                    _venta = "AGOTADO"

                if scooter.active == True:
                    element = Element(
                        title=scooter.serial_code,
                        image_url=list_url_motos[cont],
                        subtitle='{}-{}'.format(scooter.box,_venta),
                        buttons=[
                            PostbackButton(
                                title="REGRESAR",
                                payload=constants.CATEGORYS_M
                            ),
                            PostbackButton(
                                title="INICIO",
                                payload=constants.START
                            ),
                        ]
                    )
                    elements.append(element)
                    cont += 1
            template = GenericTemplate(
                elements=elements
            )
            attachment = TemplateAttachment(template=template)
            message = Message(attachment=attachment)
            responses.append(Components.typing(responses, self.event.sender))
            responses.append(MessageRequest(self.event.sender, message))
        else:
            self.typing()
            responses = list()
            replies = QuickReplies(
                replies=[
                    TextReply(
                        image_url="https://goo.gl/Rg33Yq",
                        title="MENU INICIO",
                        payload=constants.START,
                    )
                ]
            )
            message = Message(
                text="Ups, 😱 lamentamos decirte que no hay motocicletas Scooter registradas",
                quick_replies=replies
            )
            responses.append(MessageRequest(self.event.sender, message))
        self.messenger.post_message_queue(responses)

    def render_show_moto_crucero(self):
        self.typing()

        motos_crucero = Motorcycle.objects.all().filter(type = "CRUCERO")

        _crucero = 0

        for m_active in motos_crucero:
            if m_active.active == True and m_active.type == "CRUCERO":
                _crucero +=1 

        print("CANTIDAD CRUCERO", _crucero)

        list_url_motos = [
            'https://goo.gl/y3Hym7',
            'https://goo.gl/Q8UCXk',
            'https://goo.gl/76utQ6',
            'https://goo.gl/X9PDCI',
            'https://goo.gl/knZMpb',
            'https://goo.gl/vJwjcn',
            'https://goo.gl/CbGJWm',
            'https://goo.gl/PIbDBV',
            'https://goo.gl/SSvIoR',
            'https://goo.gl/opMbeu',
            'https://goo.gl/KPfjnI',
            'https://goo.gl/GdgDbF',
            'https://goo.gl/Vd0BFC'
            'https://goo.gl/Q7799l',
            'https://goo.gl/09oGyc'
        ]

        responses = list()
        elements = []

        if _crucero > 0 and _crucero <= 10:
            message = Message(text="Aqui te muestro las motocicletas de Tipo Crucero", )
            responses.append(MessageRequest(self.event.sender, message))
            cont = 1
            for crucero in motos_crucero:
                if crucero.stock > 0:
                    _venta = "DISPONIBLE"
                else:
                    _venta = "AGOTADO"

                if crucero.active == True:
                    element = Element(
                        title=crucero.serial_code,
                        image_url=list_url_motos[cont],
                        subtitle='{}-{}'.format(crucero.box,_venta),
                        buttons=[
                            PostbackButton(
                                title="REGRESAR",
                                payload=constants.CATEGORYS_M
                            ),
                            PostbackButton(
                                title="INICIO",
                                payload=constants.START
                            ),
                        ]
                    )
                    elements.append(element)
                    cont += 1
            template = GenericTemplate(
                elements=elements
            )
            attachment = TemplateAttachment(template=template)
            message = Message(attachment=attachment)
            responses.append(Components.typing(responses, self.event.sender))
            responses.append(MessageRequest(self.event.sender, message))
        else:
            self.typing()
            responses = list()
            replies = QuickReplies(
                replies=[
                    TextReply(
                        image_url="https://goo.gl/Rg33Yq",
                        title="MENU INICIO",
                        payload=constants.START,
                    )
                ]
            )
            message = Message(
                text="Ups, 😱 lamentamos decirte que no hay motocicletas Crucero registradas",
                quick_replies=replies
            )
            responses.append(MessageRequest(self.event.sender, message))
        self.messenger.post_message_queue(responses)


    def render_show_moto_chooper(self):
        self.typing()

        motos_chooper = Motorcycle.objects.all().filter(type = "CHOOPER")

        _chooper = 0

        for m_active in motos_chooper:
            if m_active.active == True and m_active.type == "CHOOPER":
                _chooper +=1 

        print("CANTIDAD CHOOPER", _chooper)

        list_url_motos = [
            'https://goo.gl/76utQ6',
            'https://goo.gl/SSvIoR',
            'https://goo.gl/KPfjnI',
            'https://goo.gl/X9PDCI',
            'https://goo.gl/vJwjcn',
            'https://goo.gl/CbGJWm',
            'https://goo.gl/PIbDBV',
            'https://goo.gl/Vd0BFC'
            'https://goo.gl/GdgDbF',
            'https://goo.gl/opMbeu',
            'https://goo.gl/Q7799l',
            'https://goo.gl/y3Hym7',
            'https://goo.gl/09oGyc',
            'https://goo.gl/Q8UCXk',
            'https://goo.gl/knZMpb'
        ]

        responses = list()
        elements = []

        if _chooper > 0 and _chooper <= 10:
            message = Message(text="Aqui te muestro las motocicletas de Tipo Chooper", )
            responses.append(MessageRequest(self.event.sender, message))
            cont = 1
            for chooper in motos_chooper:
                if chooper.stock > 0:
                    _venta = "DISPONIBLE"
                else:
                    _venta = "AGOTADO"

                if chooper.active == True:
                    element = Element(
                        title=chooper.serial_code,
                        image_url=list_url_motos[cont],
                        subtitle='{}-{}'.format(chooper.box,_venta),
                        buttons=[
                            PostbackButton(
                                title="REGRESAR",
                                payload=constants.CATEGORYS_M
                            ),
                            PostbackButton(
                                title="INICIO",
                                payload=constants.START
                            ),
                        ]
                    )
                    elements.append(element)
                    cont += 1
            template = GenericTemplate(
                elements=elements
            )
            attachment = TemplateAttachment(template=template)
            message = Message(attachment=attachment)
            responses.append(Components.typing(responses, self.event.sender))
            responses.append(MessageRequest(self.event.sender, message))
        else:
            self.typing()
            responses = list()
            replies = QuickReplies(
                replies=[
                    TextReply(
                        image_url="https://goo.gl/Rg33Yq",
                        title="MENU INICIO",
                        payload=constants.START,
                    )
                ]
            )
            message = Message(
                text="Ups, 😱 lamentamos decirte que no hay motocicletas Custom registradas",
                quick_replies=replies
            )
            responses.append(MessageRequest(self.event.sender, message))
        self.messenger.post_message_queue(responses)

    def render_show_moto_custom(self):
        self.typing()

        motos_custom = Motorcycle.objects.all().filter(type = "CUSTOM")

        _custom = 0

        for m_active in motos_custom:
            if m_active.active == True and m_active.type == "CUSTOM":
                _custom +=1 

        print("CANTIDAD CUSTOM", _custom)

        list_url_motos = [
            'https://goo.gl/76utQ6',
            'https://goo.gl/SSvIoR',
            'https://goo.gl/KPfjnI',
            'https://goo.gl/X9PDCI',
            'https://goo.gl/vJwjcn',
            'https://goo.gl/CbGJWm',
            'https://goo.gl/PIbDBV',
            'https://goo.gl/Vd0BFC'
            'https://goo.gl/GdgDbF',
            'https://goo.gl/opMbeu',
            'https://goo.gl/Q7799l',
            'https://goo.gl/y3Hym7',
            'https://goo.gl/09oGyc',
            'https://goo.gl/Q8UCXk',
            'https://goo.gl/knZMpb'
        ]

        responses = list()
        elements = []

        if _custom > 0 and _custom <= 10:
            message = Message(text="Aqui te muestro las motocicletas de Tipo Custom", )
            responses.append(MessageRequest(self.event.sender, message))
            cont = 1
            for custom in motos_custom:
                if custom.stock > 0:
                    _venta = "DISPONIBLE"
                else:
                    _venta = "AGOTADO"

                if custom.active == True:
                    element = Element(
                        title=custom.serial_code,
                        image_url=list_url_motos[cont],
                        subtitle='{}-{}'.format(custom.box,_venta),
                        buttons=[
                            PostbackButton(
                                title="REGRESAR",
                                payload=constants.CATEGORYS_M
                            ),
                            PostbackButton(
                                title="INICIO",
                                payload=constants.START
                            ),
                        ]
                    )
                    elements.append(element)
                    cont += 1
            template = GenericTemplate(
                elements=elements
            )
            attachment = TemplateAttachment(template=template)
            message = Message(attachment=attachment)
            responses.append(Components.typing(responses, self.event.sender))
            responses.append(MessageRequest(self.event.sender, message))
        else:
            self.typing()
            responses = list()
            replies = QuickReplies(
                replies=[
                    TextReply(
                        image_url="https://goo.gl/Rg33Yq",
                        title="MENU INICIO",
                        payload=constants.START,
                    )
                ]
            )
            message = Message(
                text="Ups, 😱 lamentamos decirte que no hay motocicletas Custom registradas",
                quick_replies=replies
            )
            responses.append(MessageRequest(self.event.sender, message))
        self.messenger.post_message_queue(responses)

    def render_show_moto_sidecar(self):
        self.typing()

        motos_sidecar = Motorcycle.objects.all().filter(type = "SIDECAR")

        _sidecar = 0

        for m_active in motos_sidecar:
            if m_active.active == True and m_active.type == "SIDECAR":
                _sidecar +=1 

        print("CANTIDAD SIDECAR", _sidecar)

        list_url_motos = [
            'https://goo.gl/76utQ6',
            'https://goo.gl/SSvIoR',
            'https://goo.gl/KPfjnI',
            'https://goo.gl/X9PDCI',
            'https://goo.gl/vJwjcn',
            'https://goo.gl/CbGJWm',
            'https://goo.gl/PIbDBV',
            'https://goo.gl/Vd0BFC'
            'https://goo.gl/GdgDbF',
            'https://goo.gl/opMbeu',
            'https://goo.gl/Q7799l',
            'https://goo.gl/y3Hym7',
            'https://goo.gl/09oGyc',
            'https://goo.gl/Q8UCXk',
            'https://goo.gl/knZMpb'
        ]

        responses = list()
        elements = []

        if _sidecar > 0 and _sidecar <= 10:
            message = Message(text="Aqui te muestro las motocicletas de Tipo Sidecar", )
            responses.append(MessageRequest(self.event.sender, message))
            cont = 1
            for sidecar in motos_sidecar:
                if sidecar.stock > 0:
                    _venta = "DISPONIBLE"
                else:
                    _venta = "AGOTADO"

                if sidecar.active == True:
                    element = Element(
                        title=sidecar.serial_code,
                        image_url=list_url_motos[cont],
                        subtitle='{}-{}'.format(sidecar.box,_venta),
                        buttons=[
                            PostbackButton(
                                title="REGRESAR",
                                payload=constants.CATEGORYS_M
                            ),
                            PostbackButton(
                                title="INICIO",
                                payload=constants.START
                            ),
                        ]
                    )
                    elements.append(element)
                    cont += 1
            template = GenericTemplate(
                elements=elements
            )
            attachment = TemplateAttachment(template=template)
            message = Message(attachment=attachment)
            responses.append(Components.typing(responses, self.event.sender))
            responses.append(MessageRequest(self.event.sender, message))
        else:
            self.typing()
            responses = list()
            replies = QuickReplies(
                replies=[
                    TextReply(
                        image_url="https://goo.gl/Rg33Yq",
                        title="MENU INICIO",
                        payload=constants.START,
                    )
                ]
            )
            message = Message(
                text="Ups, 😱 lamentamos decirte que no hay motocicletas Sidecar registradas",
                quick_replies=replies
            )
            responses.append(MessageRequest(self.event.sender, message))
        self.messenger.post_message_queue(responses)

    def render_show_moto_touring(self):
        self.typing()

        motos_touring = Motorcycle.objects.all().filter(type = "TOURING")

        _touring = 0

        for m_active in motos_touring:
            if m_active.active == True and m_active.type == "TOURING":
                _touring +=1 

        print("CANTIDAD TOURING", _touring)

        list_url_motos = [
            'https://goo.gl/76utQ6',
            'https://goo.gl/SSvIoR',
            'https://goo.gl/KPfjnI',
            'https://goo.gl/X9PDCI',
            'https://goo.gl/vJwjcn',
            'https://goo.gl/CbGJWm',
            'https://goo.gl/PIbDBV',
            'https://goo.gl/Vd0BFC'
            'https://goo.gl/GdgDbF',
            'https://goo.gl/opMbeu',
            'https://goo.gl/Q7799l',
            'https://goo.gl/y3Hym7',
            'https://goo.gl/09oGyc',
            'https://goo.gl/Q8UCXk',
            'https://goo.gl/knZMpb'
        ]

        responses = list()
        elements = []

        if _touring > 0 and _touring <= 10:
            message = Message(text="Aqui te muestro las motocicletas de Tipo Touring", )
            responses.append(MessageRequest(self.event.sender, message))
            cont = 1
            for touring in motos_touring:
                if touring.stock > 0:
                    _venta = "DISPONIBLE"
                else:
                    _venta = "AGOTADO"

                if touring.active == True:
                    element = Element(
                        title=touring.serial_code,
                        image_url=list_url_motos[cont],
                        subtitle='{}-{}'.format(touring.box,_venta),
                        buttons=[
                            PostbackButton(
                                title="REGRESAR",
                                payload=constants.CATEGORYS_M
                            ),
                            PostbackButton(
                                title="INICIO",
                                payload=constants.START
                            ),
                        ]
                    )
                    elements.append(element)
                    cont += 1
            template = GenericTemplate(
                elements=elements
            )
            attachment = TemplateAttachment(template=template)
            message = Message(attachment=attachment)
            responses.append(Components.typing(responses, self.event.sender))
            responses.append(MessageRequest(self.event.sender, message))
        else:
            self.typing()
            responses = list()
            replies = QuickReplies(
                replies=[
                    TextReply(
                        image_url="https://goo.gl/Rg33Yq",
                        title="MENU INICIO",
                        payload=constants.START,
                    )
                ]
            )
            message = Message(
                text="Ups, 😱 lamentamos decirte que no hay motocicletas Touring registradas",
                quick_replies=replies
            )
            responses.append(MessageRequest(self.event.sender, message))
        self.messenger.post_message_queue(responses)

    def render_show_moto_racer(self):
        self.typing()

        motos_racer = Motorcycle.objects.all().filter(type = "RACER")

        _racer = 0

        for m_active in motos_racer:
            if m_active.active == True and m_active.type == "RACER":
                _racer +=1 

        print("CANTIDAD RACER", _racer)

        list_url_motos = [
            'https://goo.gl/76utQ6',
            'https://goo.gl/SSvIoR',
            'https://goo.gl/KPfjnI',
            'https://goo.gl/X9PDCI',
            'https://goo.gl/vJwjcn',
            'https://goo.gl/CbGJWm',
            'https://goo.gl/PIbDBV',
            'https://goo.gl/Vd0BFC'
            'https://goo.gl/GdgDbF',
            'https://goo.gl/opMbeu',
            'https://goo.gl/Q7799l',
            'https://goo.gl/y3Hym7',
            'https://goo.gl/09oGyc',
            'https://goo.gl/Q8UCXk',
            'https://goo.gl/knZMpb'
        ]

        responses = list()
        elements = []

        if _racer > 0 and _racer <= 10:
            message = Message(text="Aqui te muestro las motocicletas de Tipo Racer", )
            responses.append(MessageRequest(self.event.sender, message))
            cont = 1
            for racer in motos_racer:
                if racer.stock > 0:
                    _venta = "DISPONIBLE"
                else:
                    _venta = "AGOTADO"

                if racer.active == True:
                    element = Element(
                        title=racer.serial_code,
                        image_url=list_url_motos[cont],
                        subtitle='{}-{}'.format(racer.box,_venta),
                        buttons=[
                            PostbackButton(
                                title="REGRESAR",
                                payload=constants.CATEGORYS_M
                            ),
                            PostbackButton(
                                title="INICIO",
                                payload=constants.START
                            ),
                        ]
                    )
                    elements.append(element)
                    cont += 1
            template = GenericTemplate(
                elements=elements
            )
            attachment = TemplateAttachment(template=template)
            message = Message(attachment=attachment)
            responses.append(Components.typing(responses, self.event.sender))
            responses.append(MessageRequest(self.event.sender, message))
        else:
            self.typing()
            responses = list()
            replies = QuickReplies(
                replies=[
                    TextReply(
                        image_url="https://goo.gl/Rg33Yq",
                        title="MENU INICIO",
                        payload=constants.START,
                    )
                ]
            )
            message = Message(
                text="Ups, 😱 lamentamos decirte que no hay motocicletas Racer registradas",
                quick_replies=replies
            )
            responses.append(MessageRequest(self.event.sender, message))
        self.messenger.post_message_queue(responses)

    def render_show_moto_trial(self):
        self.typing()

        motos_trial = Motorcycle.objects.all().filter(type = "TRIAL")

        _trial = 0

        for m_active in motos_trial:
            if m_active.active == True and m_active.type == "TRIAL":
                _trial +=1 

        print("CANTIDAD TRIAL", _trial)

        list_url_motos = [
            'https://goo.gl/76utQ6',
            'https://goo.gl/SSvIoR',
            'https://goo.gl/KPfjnI',
            'https://goo.gl/X9PDCI',
            'https://goo.gl/vJwjcn',
            'https://goo.gl/CbGJWm',
            'https://goo.gl/PIbDBV',
            'https://goo.gl/Vd0BFC'
            'https://goo.gl/GdgDbF',
            'https://goo.gl/opMbeu',
            'https://goo.gl/Q7799l',
            'https://goo.gl/y3Hym7',
            'https://goo.gl/09oGyc',
            'https://goo.gl/Q8UCXk',
            'https://goo.gl/knZMpb'
        ]

        responses = list()
        elements = []

        if _trial > 0 and _trial <= 10:
            message = Message(text="Aqui te muestro las motocicletas de Tipo Trial", )
            responses.append(MessageRequest(self.event.sender, message))
            cont = 1
            for trial in motos_trial:
                if trial.stock > 0:
                    _venta = "DISPONIBLE"
                else:
                    _venta = "AGOTADO"

                if trial.active == True:
                    element = Element(
                        title=trial.serial_code,
                        image_url=list_url_motos[cont],
                        subtitle='{}-{}'.format(trial.box,_venta),
                        buttons=[
                            PostbackButton(
                                title="REGRESAR",
                                payload=constants.CATEGORYS_M
                            ),
                            PostbackButton(
                                title="INICIO",
                                payload=constants.START
                            ),
                        ]
                    )
                    elements.append(element)
                    cont += 1
            template = GenericTemplate(
                elements=elements
            )
            attachment = TemplateAttachment(template=template)
            message = Message(attachment=attachment)
            responses.append(Components.typing(responses, self.event.sender))
            responses.append(MessageRequest(self.event.sender, message))
        else:
            self.typing()
            responses = list()
            replies = QuickReplies(
                replies=[
                    TextReply(
                        image_url="https://goo.gl/Rg33Yq",
                        title="MENU INICIO",
                        payload=constants.START,
                    )
                ]
            )
            message = Message(
                text="Ups, 😱 lamentamos decirte que no hay motocicletas Trial registradas",
                quick_replies=replies
            )
            responses.append(MessageRequest(self.event.sender, message))
        self.messenger.post_message_queue(responses)

    def render_promotions(self):
        self.typing()

        promociones = Promociones.objects.all().filter(active = True)

        responses = list()
        elements = []

        if promociones.count() > 0 and promociones.count() <= 10:
            message = Message(text="Hola 😄 aqui te muestro las Promociones 🏍 ", )
            responses.append(MessageRequest(self.event.sender, message))

            for promocion in promociones:
                if promocion.active == True:
                    element = Element(
                        title=promocion.nombre,
                        image_url="https://goo.gl/OQGTtF",
                        subtitle="USM - PROMOCIONES",
                        buttons=[
                            URLButton(
                                title="VER DETALLE",
                                url=promocion.url_promocion
                            ),
                            PostbackButton(
                                title="INICIO",
                                payload=constants.START
                            ),
                        ]
                    )
                    elements.append(element)
            template = GenericTemplate(
                elements=elements
            )
            attachment = TemplateAttachment(template=template)
            message = Message(attachment=attachment)
            responses.append(Components.typing(responses, self.event.sender))
            responses.append(MessageRequest(self.event.sender, message))
        else:
            self.typing()
            responses = list()
            replies = QuickReplies(
                replies=[
                    TextReply(
                        image_url="https://goo.gl/Rg33Yq",
                        title="MENU INICIO",
                        payload=constants.START,
                    )
                ]
            )
            message = Message(
                text="Contarte que no hay Promociones Habilitadas 😱, estate atento pronto habra promociones 😉 👍 ",
                quick_replies=replies
            )
            responses.append(MessageRequest(self.event.sender, message))
        self.messenger.post_message_queue(responses)

    def render_accesories(self):
        self.typing()

        accesorios = Repuesto.objects.all().filter(active = True)

        responses = list()
        elements = []

        if accesorios.count() > 0 and accesorios.count() <= 10:
            message = Message(text="Hola 😄 aqui te muestro los accesorios para motocicletas 🏍 ", )
            responses.append(MessageRequest(self.event.sender, message))

            for accesorio in accesorios:
                if accesorio.stock > 0:
                    _venta = "DISPONIBLE"
                else:
                    _venta = "AGOTADO"
                if accesorio.active == True:
                    element = Element(
                        title=accesorio.name,
                        image_url="https://goo.gl/5EGLWp",
                        subtitle=_venta,
                        buttons=[
                            PostbackButton(
                                title="INICIO",
                                payload=constants.START
                            ),
                            PostbackButton(
                                title="REGRESAR",
                                payload=constants.PRODUCTS
                            ),
                        ]
                    )
                    elements.append(element)
            template = GenericTemplate(
                elements=elements
            )
            attachment = TemplateAttachment(template=template)
            message = Message(attachment=attachment)
            responses.append(Components.typing(responses, self.event.sender))
            responses.append(MessageRequest(self.event.sender, message))
        else:
            self.typing()
            responses = list()
            replies = QuickReplies(
                replies=[
                    TextReply(
                        image_url="https://goo.gl/Rg33Yq",
                        title="MENU INICIO",
                        payload=constants.START,
                    )
                ]
            )
            message = Message(
                text="No se pudo mostrar los Accesorios 😱",
                quick_replies=replies
            )
            responses.append(MessageRequest(self.event.sender, message))
        self.messenger.post_message_queue(responses)

    def render_process_user(self):
        responses = list()
        self.typing()

        if hasattr(self, "player_added"):
            text = self.player_added + " es invalido vuelve a intentarlo"
        else:
            text = "Porfavor ingresa tu Cedula de Identidad"

        replies = QuickReplies(
            replies=[
                TextReply(
                    image_url="https://goo.gl/6t7mb7",
                    title="CANCELAR",
                    payload=constants.START_DESTROY,
                ),

            ]
        )
        message = Message(
            text=text,
            quick_replies=replies
        )
        responses.append(MessageRequest(self.event.sender, message))
        self.messenger.post_message_queue(responses)

    def render_list_asistencias(self):
        self.typing()

        _user = self.session["store"]["users_ci"]

        print("user ", _user)
        print("type ", type(_user))

        for x in _user:
            _select_id = x['ci']

        _select_id = int(_select_id)

        asistencias = Reparacion.objects.all().filter(habilitado = True)

        contador = 0
        for asistencia in asistencias:
            if _select_id == int(asistencia.cliente.cedula):
                contador +=1


        print("CONTADOR ", contador)


        responses = list()
        elements = []

        if contador > 0 and contador <= 10:
            message = Message(text="Hola 😄 aqui esta el listado de tus asistencias ", )
            responses.append(MessageRequest(self.event.sender, message))

            for asistance in asistencias:
                if _select_id == int(asistance.cliente.cedula) and asistance.estado == "PENDIENTE":
                    element = Element(
                        title=asistance.placa.upper(),
                        image_url="https://goo.gl/7c63UD",
                        subtitle="Devolucion "+ str(asistance.fin_reparacion),
                        buttons=[
                            PostbackButton(
                                title="TERMINAR",
                                payload=constants.START_DESTROY
                            ),
                            PostbackButton(
                                title="VOLVER A CONSULTAR",
                                payload=constants.ADD_CEDULA_DESTROY
                            ),
                        ]
                    )
                    elements.append(element)
            template = GenericTemplate(
                elements=elements
            )
            attachment = TemplateAttachment(template=template)
            message = Message(attachment=attachment)
            responses.append(Components.typing(responses, self.event.sender))
            responses.append(MessageRequest(self.event.sender, message))
        else:
            self.typing()
            responses = list()
            replies = QuickReplies(
                replies=[
                    TextReply(
                        image_url="https://goo.gl/Rg33Yq",
                        title="MENU INICIO",
                        payload=constants.START,
                    )
                ]
            )
            message = Message(
                text="No se pudo mostrar Asistencia Mecanica 😱",
                quick_replies=replies
            )
            responses.append(MessageRequest(self.event.sender, message))
        self.messenger.post_message_queue(responses)


    def render_login(self):
        template = GenericTemplate(
            elements=[
                Element(
                    title="Iniciar Sesión",
                    subtitle="y Que siga la Fiesta",
                    buttons=[
                        LoginButton(
                            url=self.get_url("/facebook/authorize/%s/" % self.event.sender.id)
                        )
                    ]
                )
            ]
        )

        attachment = TemplateAttachment(template=template)
        message = Message(attachment=attachment)
        response =  MessageRequest(self.event.sender, message)
        self.messenger.post_message(response)


    def render_logged_in(self):
        responses = list()
        message = Message(text=" Login con Exito 😄")
        responses.append(MessageRequest(self.event.sender, message))
        self.messenger.post_message_queue(responses)


    def render_message(self, text):
        self.typing()
        responses = list()
        message = Message(text=text)
        responses.append(MessageRequest(self.event.sender, message))
        self.messenger.post_message_queue(responses)

# ----------------------------------------------------------------------


    def render_category_list(self):
        # responses = list()
        # message = Message(text="Escribe que tipo de bebida")
        # responses.append(Components.typing(responses, self.event.sender))
        # responses.append(MessageRequest(self.event.sender, message))
        pass



