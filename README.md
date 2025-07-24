# CRUD-DJANGO

# 📚 Proyecto: CRUD de Gestión de Libros

Este proyecto tiene como finalidad crear una aplicación web con un **CRUD** (Crear, Leer, Actualizar y Eliminar) para gestionar una lista de libros, almacenando información como el **título**, **autor**, **género** y **fecha de publicación**.

![Gestión de Libros](https://th.bing.com/th/id/R.7f3efec26e44187eaa8dbb84850eea50?rik=UfxFSQys%2bqNexw&riu=http%3a%2f%2f3.bp.blogspot.com%2f-LGiCpXy1NR8%2fVZ8OeHWu07I%2fAAAAAAAABwU%2fcoXh_1OFPbM%2fs1600%2fbooks-wallpapers-hd-free-download.jpg&ehk=HRbJ24SuXkL9NGQnZp%2f0c96Aj%2blfZhftxGccTf34AnI%3d&risl=&pid=ImgRaw&r=0)

---

## 🧠 Sprint Goal

Desarrollar una aplicación web funcional que permita al usuario:
- **Agregar** nuevos libros.
- **Visualizar** la lista de libros registrados.
- **Editar** la información de un libro existente.
- **Eliminar** un libro.

---

## 🚀 Sprint Backlog

| Tarea                                                                                  | Gadiel (G) | Edson (ER) | Christopher (CS) |
|----------------------------------------------------------------------------------------|:----------:|:----------:|:----------------:|
| Crear estructura HTML para mostrar la lista de libros y formulario de creación/edición |     X      |            |                  |
| Estilizar la página con diseño responsive                                              |     X      |            |                  |
| Implementar lógica con JavaScript para crear y mostrar libros                          |            |     X      |                  |
| Implementar función de actualización y edición de libros                               |            |            |        X         |
| Implementar función para eliminar libros                                               |            |            |        X         |
| Manejar validaciones de campos (no vacíos, fechas correctas)                           |            |     X      |                  |
| Guardar datos en localStorage (opcional)                                               |            |            |        X         |
| Subir proyecto a GitHub                                                                |            |     X      |                  |
| Documentar en el README.md                                                             |            |     X      |                  |

---

## 👥 Roles del Equipo

| Rol              | Nombre del integrante  | Función principal                                       |
|------------------|------------------------|---------------------------------------------------------|
| Scrum Master     | Alfredo Gonzales       | Supervisa el avance del equipo y organiza reuniones     |
| Product Owner    | Diego Espinoza         | Define las funcionalidades clave del CRUD               |
| Developer 1      | Gadiel Collazos        | Crea la interfaz HTML y aplica el diseño responsivo     |
| Developer 2      | Christopher Sosa       | Creador de la base de datos  |
| Developer 3      | Edson Rojas            | Lógica de creación de libros y documentación            |

---

## 🛠 Tecnologías Utilizadas

- **HTML5**
- **CSS3**
- **Python**
- **Django**        

---

## 📦 Funcionalidades del CRUD

- **Crear libro:** Agregar un nuevo libro con título, autor, género y fecha de publicación.
- **Listar libros:** Mostrar todos los libros en una tabla dinámica.
- **Editar libro:** Modificar la información de un libro existente.
- **Eliminar libro:** Borrar un libro de la lista.
- **Validaciones:** Comprobar que los campos no estén vacíos y que la fecha sea válida.

---

## 🔗 Link de la Demo

*(Pendiente: se colocará el enlace una vez desplegado en GitHub Pages)

---

## 📘 Cómo usar la aplicación

1. **Abre el archivo `index.html` en tu navegador.**  
   Asegúrate de que los archivos `styles.css` (en `css/`) y `app.py` estén enlazados correctamente.

2. **Interfaz principal:**
   - Rellena el formulario para agregar un nuevo libro.
   - Los libros aparecen en una tabla dinámica.
   - Cada libro cuenta con botones de **Editar** y **Eliminar**.

3. **Características:**
   - ✅ CRUD completo en memoria (localStorage opcional).
   - ✅ Validaciones de campos.
   - ✅ Diseño responsive.

---
## 👨‍💻 Futuras Mejoras

- Conexión a una base de datos real (por ejemplo, Firebase o una API REST).
- Paginación y búsqueda por título/autor.
- Exportar datos en formato JSON o CSV.