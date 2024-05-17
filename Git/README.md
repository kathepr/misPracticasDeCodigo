COMANDOS:

1. Entrar a una carpeta: cd
2. Salir de la carpeta: cd ..
3. Crear carpeta: mkdir nombreCarpeta
4. Eliminar carpetas vacias: rmdir nombreDirectorio
5. Eliminar carpetas no vacias: rm -r nombreDirectorio
5. Entrar a un archivo: git checkout nombreArchivo

6. Inicializar git: git init
7. Ver que archivos hay dentro de la carpeta: ls
8. Pasar archivo a staged changes: git add nombreArchivo
9. Pasar todos los archivos a staged changes: git add .
10. Ver información sobre directorio de trabajo: git status

11. Quitar archivos de staged changes: git rm --cached nombreArchivo

12. Configurar credenciales:
* git config --global user.name "nombreUsuarioGithub"
* git config --global user.email "exmple@gmail.com"
* git config --global core.editor "code --wait"


13. Conventional commits:
* git commit -m "mensaje"


| Tipo de Commit | Descripción | Gitmoji |

| feat | Se comienza nuevo proyecto | :tada: |
| feat | Añadir una nueva característica al código | :sparkles: |
| fix | Corregir un error o bug | :bug: |
| docs | Cambios o mejoras en la documentación | :memo: |
| style | Cambios en el formato del código que no afectan su comportamiento | :art: |
| refactor | Cambios en el código que mejoran su estructura o legibilidad | :recycle: |
| test | Adiciones o modificaciones en pruebas | :white_check_mark: |
| chore | Cambios en tareas de construcción o configuración | :wrench: |


14. Si tengo un archivo en staged changes y lo eliminé de mi área local, lo puedo restaurar de esta manera: git restore nombreArchivo

15. Si queremos ver la diferencia entre el archivo en area de preparacion y el area de trabajo se usa: git diff --staged

16. Para ver el historial de commits (junto con sus ID's): git log --oneline


17. Para comprar dos commits (ver diferencia): git diff idCommit1 idCommit2




MODIFICAR Y DESHACER COMMITS:

18. Modificar el mensaje del commit: git commit --amend

19. Añadir archivos olvidados al commit: Se agregan a area de preparacion los nuevos archivos y luego escribes: git commit --amend

20. Deshacer el commit, pero conservando los cambios en el área de preparación y en el directorio de trabajo.: git reset --soft idCommit

21. Deshacer el commit y mover los cambios que se deshacen al área de preparación. Sin embargo, los cambios no se deshacen en el directorio de trabajo, lo que significa que los archivos mantendrán los cambios que tenían en el commit que se deshizo, pero no estarán preparados para el siguiente commit: git reset --mixed idCommit

22. Deshacer el commit y descartar los cambios realizados en los archivos en el área de preparación y en el directorio de trabajo: git reset --hard idCommit





RAMAS: 

23. Ver todas las ramas existentes: git branch

24. Crear una rama: git branch nombreRamaNueva

25. Para pasarme a otra rama: 
* git checkout nombreRama
* git switch : es la mas utilizada

26. Para crear la rama localmente y cambiar a ella al mismo tiempo: 
* git checkout -b nombreRamaNueva
* git switch -c nombreRamaNueva       

27. Eliminar rama: git branch -d nombreRama

28. Cambiar nombre de una rama si estamos parados en otras ramas del proyecto: git branch -m nombreRama nombreNuevoParaRama

29. Cambiar nombre de una rama si estamos parados en la rama del proyecto: git branch -m nombreNuevoParaRama



MERGE FUSIONAR RAMAS:

30. Debo estar posicionada en la rama que deseo fusionar: 
* En este caso me paro en master y luego: git merge nombreRamaQueQuieroFusionarEnMaster

31. Si quiero deshacer una fusion:
* git reset --hard idRamaQueHabiaFusionado




RESOLVER CONFLICTOS ENTRE RAMAS:


32. En view ingresa a Source Control o puedes oprimir: Ctrol Shift G

33. Abrir el merge editor:

Para abrir el merge editor en Visual Studio Code, puedes hacer lo siguiente:
Haz clic en el botón Accept (Aceptar) en el lado izquierdo de la barra de título del editor. Este botón aparece cuando abres un archivo con conflictos.
Alternativamente, puedes hacer clic derecho en el archivo en el panel de control de Git y seleccionar Open Changes.



RECUPERAR CAMBIOS PERDIDOS O REVERTIR ESTADO ANTERIOR DEL REPOSITORIO:

* git reflog : Permite ver un registro de referencia de HEAD, que incluye las referencias de las ramas y los cambios de historial de commits que han ocurrido en tu repositorio local

* Luego se puede usar un git reset --hard idReferenciaCommit







GITHUB:

1. Clonar un repositorio:
* git clone URLrepositorio (HTTPS)

2. Subir cambios al servidor remoto:
* git push 

3. Bajar los cambios que se encuentran en el servidor y fusionarlos directamente a la rama local:
* git pull

4. Bajar los cambios que se encuentran en el servidor pero NO LOS FUSIONA localmente:
* git fetch
* git switch --detach origin/master: me crea una rama temporal para visualizar los cambios.

* Si decido que los cambios me sirven, volvemos a la rama master: git switch master y podemos hacer git pull y solucionar conflictos