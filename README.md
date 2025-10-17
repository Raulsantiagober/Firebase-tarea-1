Este proyecto implementa un sistema de **gestión de cuentas bancarias** utilizando **Firebase Realtime Database** como backend y **Python** con arquitectura por capas (Clean Architecture).

Permite realizar todas las operaciones CRUD:
- Crear una cuenta
- Consultar una cuenta
- Actualizar saldo
- Eliminar cuenta
- Listar todas las cuentas
Evidencia del funcionamiento

A continuación se muestra el **menú principal** del programa, el cual se ejecuta en la consola tras correr el comando
<img width="1155" height="884" alt="Captura de pantalla 2025-10-16 232152" src="https://github.com/user-attachments/assets/92bc9f07-cf8b-440a-ae56-10391f97afae" />
<img width="735" height="572" alt="Captura de pantalla 2025-10-16 232221" src="https://github.com/user-attachments/assets/879d5a24-743a-4ad2-a15d-1ced6a700e3d" />
<img width="1310" height="666" alt="Captura de pantalla 2025-10-16 232301" src="https://github.com/user-attachments/assets/3d6601e0-ffec-4226-93fe-1118e791591f" />

En las siguientes imagenes se muestra cómo las cuentas creadas desde el programa se almacenan correctamente en la **Firebase Realtime Database**.

Cada cuenta contiene los siguientes campos:
- **numero:** identificador único de la cuenta  
- **titular:** nombre del propietario  
- **saldo:** monto actual en la cuenta  

<img width="559" height="299" alt="Captura de pantalla 2025-10-16 232359" src="https://github.com/user-attachments/assets/701f5ac7-8783-42a3-8e94-94d1fd957571" />
<img width="1916" height="956" alt="Captura de pantalla 2025-10-16 223625" src="https://github.com/user-attachments/assets/09b57e11-86d0-49ee-8689-012c80386ba6" />
