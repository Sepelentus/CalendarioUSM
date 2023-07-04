# PRUEBA DE INTEGRACIÓN

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class SignInIntegrationTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='test@example.com',
            password='password123'
        )

    def test_sign_in_form_valid_data(self):
        url = reverse("accounts:signin")
        data = {
            "email": "test@example.com",
            "password": "password123"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)  # Cambiar 200 por 302
        # Aquí se pueden agregar más comprobaciones para asegurarte de que el inicio de sesión se realizó correctamente


    def test_sign_in_form_invalid_data(self):
        url = reverse("accounts:signin")
        data = {
            "email": "test@example.com",
            "password": "wrongpassword"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        # Aquí se pueden agregar más comprobaciones para asegurarte de que se manejan correctamente los datos de inicio de sesión inválidos

    def test_sign_in_form_empty_data(self):
        url = reverse("accounts:signin")
        data = {}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        # Aquí se pueden agregar más comprobaciones para asegurarte de que se manejan correctamente los datos de inicio de sesión vacíos

'''
En este ejemplo, se definen tres casos de prueba:

test_sign_in_form_valid_data: Prueba el escenario en el que se proporcionan datos de inicio de sesión válidos y se espera un inicio de sesión exitoso.
test_sign_in_form_invalid_data: Prueba el escenario en el que se proporcionan datos de inicio de sesión inválidos y se espera que se manejen correctamente.
test_sign_in_form_empty_data: Prueba el escenario en el que no se proporcionan datos de inicio de sesión y se espera que se manejen correctamente.

'''

#PRUEBA UNITARIA AUTOMATIZADA
from django.test import TestCase
from django.contrib.admin import AdminSite
from calendarapp.models import Event, EventMember
from calendarapp.admin import EventAdmin, EventMemberAdmin


class EventAdminTestCase(TestCase):
    def setUp(self):
        self.admin_site = AdminSite()
        self.event_admin = EventAdmin(Event, self.admin_site)

    def test_event_admin_list_display(self):
        list_display = self.event_admin.get_list_display(request=None)
        expected_list_display = [
            "id",
            "title",
            "user",
            "is_active",
            "is_deleted",
            "created_at",
            "updated_at",
        ]
        self.assertEqual(list_display, expected_list_display)

    def test_event_admin_list_filter(self):
        list_filter = self.event_admin.get_list_filter(request=None)
        expected_list_filter = ["is_active", "is_deleted"]
        self.assertEqual(list_filter, expected_list_filter)

    def test_event_admin_search_fields(self):
        search_fields = self.event_admin.get_search_fields(request=None)
        expected_search_fields = ["title"]
        self.assertEqual(search_fields, expected_search_fields)


class EventMemberAdminTestCase(TestCase):
    def setUp(self):
        self.admin_site = AdminSite()
        self.event_member_admin = EventMemberAdmin(EventMember, self.admin_site)

    def test_event_member_admin_list_display(self):
        list_display = self.event_member_admin.get_list_display(request=None)
        expected_list_display = ["id", "event", "user", "created_at", "updated_at"]
        self.assertEqual(list_display, expected_list_display)

    def test_event_member_admin_list_filter(self):
        list_filter = self.event_member_admin.get_list_filter(request=None)
        expected_list_filter = ["event"]
        self.assertEqual(list_filter, expected_list_filter)

'''En este ejemplo, hemos creado una clase de prueba para cada clase de administrador (EventAdmin y EventMemberAdmin). 
En el método setUp(), creamos una instancia del objeto AdminSite() y luego creamos una instancia de la clase de administrador correspondiente pasándole el modelo
 y el objeto AdminSite().

Luego, en cada clase de prueba, hemos definido métodos de prueba para verificar los atributos específicos de cada clase de administrador.

Por ejemplo, en EventAdminTestCase, verificamos los atributos list_display, list_filter y search_fields del EventAdmin para asegurarnos de que estén configurados correctamente.

De manera similar, en EventMemberAdminTestCase, verificamos los atributos list_display y list_filter del EventMemberAdmin.'''

#PRUEBA UNITARIA AUTOMATIZADA

from django.test import SimpleTestCase
from django.urls import reverse, resolve
from calendarapp import views

class CalendarAppURLTest(SimpleTestCase):
    def test_calendar_url(self):
        url = reverse("calendarapp:calendar")
        self.assertEqual(resolve(url).func.view_class, views.CalendarViewNew)

    def test_calendars_url(self):
        url = reverse("calendarapp:calendars")
        self.assertEqual(resolve(url).func.view_class, views.CalendarView)

    def test_event_new_url(self):
        url = reverse("calendarapp:event_new")
        self.assertEqual(resolve(url).func, views.create_event)

    def test_event_edit_url(self):
        url = reverse("calendarapp:event_edit", args=[1])  # Reemplaza 1 con el ID válido
        self.assertEqual(resolve(url).func.view_class, views.EventEdit)

    def test_event_detail_url(self):
        url = reverse("calendarapp:event-detail", args=[1])  # Reemplaza 1 con el ID válido
        self.assertEqual(resolve(url).func, views.event_details)

    def test_add_eventmember_url(self):
        url = reverse("calendarapp:add_eventmember", args=[1])  # Reemplaza 1 con el ID válido
        self.assertEqual(resolve(url).func, views.add_eventmember)

    def test_remove_event_url(self):
        url = reverse("calendarapp:remove_event", args=[1])  # Reemplaza 1 con el ID válido
        self.assertEqual(resolve(url).func.view_class, views.EventMemberDeleteView)

    def test_all_events_url(self):
        url = reverse("calendarapp:all_events")
        self.assertEqual(resolve(url).func.view_class, views.AllEventsListView)

    def test_running_events_url(self):
        url = reverse("calendarapp:running_events")
        self.assertEqual(resolve(url).func.view_class, views.RunningEventsListView)

    #En esta prueba de integración, se utilizan los métodos reverse y resolve de Django para obtener la URL correspondiente a cada vista y luego se verifica que la vista asociada sea la esperada.
