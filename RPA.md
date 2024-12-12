# Reto de SW RPA

## 1. **Investigar sobre DevOps**

**DevOps** (Development + Operations) es un enfoque cultural y técnico que busca integrar a los equipos de desarrollo de software y operaciones para mejorar la colaboración, la automatización y la entrega de software. 

#### **Objetivos principales de DevOps:**
- **Automatización:** Implementar pipelines para la integración continua (CI) y entrega continua (CD).
- **Colaboración:** Mejorar la comunicación entre desarrollo y operaciones.
- **Monitorización:** Supervisar aplicaciones y sistemas para garantizar su funcionamiento óptimo.
- **Cultura Ágil:** Fomentar iteraciones rápidas y retroalimentación continua.

#### **Pilares de DevOps:**
1. **Integración Continua (CI):**
   - Automatizar la construcción y prueba del código.
   - Detectar errores rápidamente.
   - Herramientas comunes: Jenkins, GitHub Actions, GitLab CI, CircleCI.

2. **Entrega Continua (CD):**
   - Automatizar el despliegue del software.
   - Proporcionar versiones confiables a producción.
   - Herramientas comunes: ArgoCD, Spinnaker, AWS CodePipeline.

3. **Infraestructura como Código (IaC):**
   - Gestionar infraestructura mediante scripts.
   - Herramientas comunes: Terraform, Ansible, CloudFormation.

4. **Monitorización y Logística:**
   - Supervisar el estado de aplicaciones y servicios.
   - Herramientas comunes: Prometheus, Grafana, ELK Stack.


## 2. **Qué comandos se pueden realizar en los archivos `.yml` (GitHub Actions)**

En los archivos `.yml` utilizados en GitHub Actions, se pueden  definir comandos que se ejecutan como pasos de un flujo de trabajo.

### **Ejemplos**

#### **Comandos básicos:**
1. **`uses`**
   - Usar una acción predefinida o de un marketplace.
   - Ejemplo:
     ```yaml
     uses: actions/checkout@v3
     ```

2. **`run`**
   - Ejecutar comandos del sistema operativo o scripts personalizados.
   - Ejemplo:
     ```yaml
     run: npm install
     ```

3. **`env`**
   - Definir variables de entorno para los pasos.
   - Ejemplo:
     ```yaml
     env:
       NODE_ENV: production
     ```

#### **Operaciones posibles:**
1. **Instalar dependencias:**
   ```yaml
   run: |
     python -m pip install -r requirements.txt
   ```

2. **Ejecutar pruebas:**
   ```yaml
   run: npm test
   ```

3. **Construir proyectos:**
   ```yaml
   run: mvn clean package
   ```

4. **Desplegar aplicaciones:**
   ```yaml
   uses: actions/deploy-pages@v1
   ```

5. **Validar código:**
   ```yaml
   run: yamllint .github/workflows/*.yml
   ```
6. **Usar filtros para seleccionar rutas específicas para pull request o push**
   Incluir con `paths` y excluir con `paths-ignore`
   ```yaml
   on:
      push:
         paths:
            - '**.js'
   ```

## 3. **Cómo funcionan los archivos `.yml`**

Los archivos `.yml` en GitHub Actions son configuraciones escritas en YAML (Yet Another Markup Language). Estas configuraciones definen flujos de trabajo automáticos que GitHub ejecuta al activarse ciertos eventos en el repositorio.

#### **Estructura básica de un archivo `.yml`:**

1. **Definir el nombre del flujo de trabajo (`name`):**
   - Es el título descriptivo del flujo de trabajo.
   ```yaml
   name: CI/CD Workflow
   ```

2. **Definir los eventos (`on`):**
   - Especifican qué eventos activan el flujo de trabajo.
   ```yaml
   on:
     push:
       branches:
         - main
     pull_request:
   ```

3. **Definir los trabajos (`jobs`):**
   - Dividen el flujo en tareas específicas (como construir, probar, o desplegar).
   ```yaml
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - name: Checkout code
           uses: actions/checkout@v3
   ```

4. **Definir los pasos (`steps`):**
   - Son comandos o acciones que se ejecutan en un trabajo.
   ```yaml
         - name: Instalar dependencias
           run: npm install
   ```-

### **Resumen del flujo de ejecución de un archivo `.yml`:**
1. **Evento:** Un evento (como `push`) activa el flujo de trabajo.
2. **Trabajo:** El flujo de trabajo ejecuta los `jobs` definidos.
3. **Pasos:** Cada `job` se descompone en pasos (`steps`) que ejecutan acciones o comandos.
