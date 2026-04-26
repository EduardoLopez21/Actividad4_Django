// Datos para la página principal (plantilla.html)
const serviciosInicio = [
    {
        titulo: "Desarrollo de Software",
        descripcion: "Creación de aplicaciones web y sistemas escalables a la medida.",
        url: "/dsf/"
    },
    {
        titulo: "Administración de Bases de Datos",
        descripcion: "Diseño, optimización y mantenimiento de bases de datos relacionales.",
        url: "/adb/"
    },
    {
        titulo: "Gestion de Redes",
        descripcion: "Implementación de infraestructuras seguras y eficientes para tu empresa.",
        url: "/gr/"
    },
    {
        titulo: "Inteligencia Artificial",
        descripcion: "Sistemas capaces de realizar tareas que normalmente requieren inteligencia humana.",
        url: "/ia/"
    }
];

// Datos diferentes para la página de Desarrollo de Software (dsf.html)
const caracteristicasDSF = [
    {
        titulo: "Java",
        descripcion: "Lenguaje orientado a objetos, multiplataforma e ideal para aplicaciones empresariales, móviles y sistemas distribuidos.",
        icono: "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/java/java-original.svg",
        url: "#"
    },
    {
        titulo: "Python",
        descripcion: "Lenguaje versátil y fácil de aprender, usado en inteligencia artificial, ciencia de datos y automatización.",
        icono: "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg",
        url: "#"
    },
    {
        titulo: "HTML",
        descripcion: "Lenguaje de marcado esencial para estructurar el contenido de todas las páginas y aplicaciones web.",
        icono: "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/html5/html5-original.svg",
        url: "#"
    },
    {
        titulo: "CSS",
        descripcion: "Lenguaje de estilos que controla el diseño visual, colores, tipografía y animaciones de sitios web.",
        icono: "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/css3/css3-original.svg",
        url: "#"
    },
    {
        titulo: "JavaScript",
        descripcion: "Lenguaje dinámico del navegador que permite crear interfaces interactivas y experiencias web en tiempo real.",
        icono: "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/javascript/javascript-original.svg",
        url: "#"
    },
    {
        titulo: "TypeScript",
        descripcion: "Superset de JavaScript con tipado estático que mejora la escalabilidad y mantenimiento de proyectos grandes.",
        icono: "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/typescript/typescript-original.svg",
        url: "#"
    },
    {
        titulo: "C#",
        descripcion: "Lenguaje de Microsoft para desarrollo de aplicaciones de escritorio, videojuegos con Unity y servicios web.",
        icono: "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/csharp/csharp-original.svg",
        url: "#"
    }
];

const caracteristicasGR = [
    {
        titulo: "Redes LAN/WAN",
        descripcion: "Diseño, configuración y mantenimiento de redes locales y de área amplia para conectar equipos.",
        icono: "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/linux/linux-original.svg",
        url: "#"
    },
    {
        titulo: "Seguridad de Red",
        descripcion: "Implementación de firewalls, VPNs y políticas de seguridad para proteger la infraestructura de red.",
        icono: "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/ssh/ssh-original-wordmark.svg",
        url: "#"
    },
    {
        titulo: "Docker",
        descripcion: "Plataforma de contenedores que permite empaquetar y desplegar aplicaciones de forma rápida y portátil.",
        icono: "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/docker/docker-original.svg",
        url: "#"
    },
    {
        titulo: "Nginx",
        descripcion: "Servidor web y proxy inverso de alto rendimiento utilizado para balanceo de carga y caché.",
        icono: "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/nginx/nginx-original.svg",
        url: "#"
    },
    {
        titulo: "Kubernetes",
        descripcion: "Sistema de orquestación de contenedores que automatiza el despliegue, escalado y gestión de aplicaciones.",
        icono: "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/kubernetes/kubernetes-original.svg",
        url: "#"
    },
    {
        titulo: "Grafana",
        descripcion: "Herramienta de monitoreo y visualización de métricas de red en tiempo real mediante dashboards.",
        icono: "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/grafana/grafana-original.svg",
        url: "#"
    },
    {
        titulo: "Ansible",
        descripcion: "Herramienta de automatización para configurar servidores, gestionar infraestructura y desplegar aplicaciones fácilmente.",
        icono: "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/ansible/ansible-original.svg",
        url: "#"
    }
];

const caracteristicasADB = [
    {
        titulo: "MySQL",
        descripcion: "Sistema de gestión de bases de datos relacional de código abierto, rápido y ampliamente utilizado.",
        icono: "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/mysql/mysql-original.svg",
        url: "#"
    },
    {
        titulo: "PostgreSQL",
        descripcion: "Base de datos relacional avanzada con soporte para consultas complejas, JSON y alta concurrencia.",
        icono: "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/postgresql/postgresql-original.svg",
        url: "#"
    },
    {
        titulo: "MongoDB",
        descripcion: "Base de datos NoSQL orientada a documentos, ideal para aplicaciones con datos flexibles y escalables.",
        icono: "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/mongodb/mongodb-original.svg",
        url: "#"
    },
    {
        titulo: "Redis",
        descripcion: "Almacén de datos en memoria usado como caché y broker de mensajes con velocidad extrema.",
        icono: "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/redis/redis-original.svg",
        url: "#"
    },
    {
        titulo: "Oracle",
        descripcion: "Sistema empresarial de bases de datos líder en el mercado corporativo con alta disponibilidad.",
        icono: "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/oracle/oracle-original.svg",
        url: "#"
    },
    {
        titulo: "SQLite",
        descripcion: "Motor de base de datos ligero y autocontenido, perfecto para aplicaciones móviles y embebidas.",
        icono: "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/sqlite/sqlite-original.svg",
        url: "#"
    },
    {
        titulo: "Firebase",
        descripcion: "Plataforma de Google con base de datos en tiempo real, autenticación y hosting para apps web.",
        icono: "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/firebase/firebase-original.svg",
        url: "#"
    },
    {
        titulo: "SQL Server",
        descripcion: "Sistema de base de datos de Microsoft con herramientas de análisis, integración y reportes avanzados.",
        icono: "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/microsoftsqlserver/microsoftsqlserver-original.svg",
        url: "#"
    }
];


// 2. LA CREACION DE TARJETAS

function crearTarjetas(listaDeDatos, idContenedor, catDinamica = null) {
    const contenedor = document.getElementById(idContenedor);

    // Si el contenedor NO existe en la página actual, detenemos la función para evitar errores
    if (!contenedor) return;

    listaDeDatos.forEach((item, index) => {
        const tarjeta = document.createElement("div");
        tarjeta.className = "tarjeta-servicio";
        tarjeta.style.cursor = (item.url && item.url !== "#") ? "pointer" : "default";

        if (item.url && item.url !== "#") {
            tarjeta.onclick = function (e) {
                if (!e.target.closest('.btn-eliminar-tarjeta')) {
                    window.location.href = item.url;
                }
            };
        }

        if (catDinamica) {
            const btnEliminar = document.createElement("a");
            btnEliminar.href = `/eliminar/?cat=${catDinamica}&idx=${index}`;
            btnEliminar.className = "btn-eliminar-tarjeta";
            btnEliminar.innerHTML = "🗑️";
            btnEliminar.title = "Eliminar servicio";
            tarjeta.appendChild(btnEliminar);
        }

        // Si el item tiene un icono, crear la imagen del logo
        if (item.icono) {
            const iconoElemento = document.createElement("img");
            iconoElemento.src = item.icono;
            iconoElemento.alt = item.titulo + " logo";
            iconoElemento.className = "tarjeta-icono";
            tarjeta.appendChild(iconoElemento);
        }

        const tituloElemento = document.createElement("h3");
        tituloElemento.textContent = item.titulo;

        const descripcionElemento = document.createElement("p");
        descripcionElemento.textContent = item.descripcion;

        tarjeta.appendChild(tituloElemento);
        tarjeta.appendChild(descripcionElemento);

        contenedor.appendChild(tarjeta);
    });
}


// 3. EJECUTAR LA FÁBRICA SEGÚN LA PÁGINA

// Le decimos a JS: Intenta buscar los contenedores en la página que estoy viendo ahorita
const divInicio = document.getElementById("contenedor-inicio");
const divDSF = document.getElementById("contenedor-dsf");
const divADB = document.getElementById("contenedor-adb");
const divGR = document.getElementById("contenedor-gr");

// Si encontró el div de inicio, dibuja los servicios principales
if (divInicio) {
    crearTarjetas(serviciosInicio, "contenedor-inicio");
    if (typeof nuevosDinamicosObj !== 'undefined' && nuevosDinamicosObj.length > 0) {
        crearTarjetas(nuevosDinamicosObj, "contenedor-inicio", "inicio");
    }
}

// Si encontró el div de Desarrollo de Software, dibuja las características de software
if (divDSF) {
    crearTarjetas(caracteristicasDSF, "contenedor-dsf");
    if (typeof nuevosDinamicosObj !== 'undefined' && nuevosDinamicosObj.length > 0) {
        crearTarjetas(nuevosDinamicosObj, "contenedor-dsf", "dsf");
    }
}

if (divADB) {
    crearTarjetas(caracteristicasADB, "contenedor-adb");
    if (typeof nuevosDinamicosObj !== 'undefined' && nuevosDinamicosObj.length > 0) {
        crearTarjetas(nuevosDinamicosObj, "contenedor-adb", "adb");
    }
}

if (divGR) {
    crearTarjetas(caracteristicasGR, "contenedor-gr");
    if (typeof nuevosDinamicosObj !== 'undefined' && nuevosDinamicosObj.length > 0) {
        crearTarjetas(nuevosDinamicosObj, "contenedor-gr", "gr");
    }
}

const divIA = document.getElementById("contenedor-ia");
if (divIA) {
    if (typeof nuevosIaDjango !== 'undefined' && nuevosIaDjango.length > 0) {
        crearTarjetas(nuevosIaDjango, "contenedor-ia", "ia");
    }
}

const divDinamico = document.getElementById("contenedor-dinamico");
if (divDinamico) {
    // Aquí sacamos el slug de la URL actual para que se pueda borrar
    // Asumimos que la URL es del tipo /servicio/slug/
    const urlParts = window.location.pathname.split('/').filter(Boolean);
    const currentSlug = urlParts.length > 1 ? urlParts[1] : null;

    if (typeof nuevosDinamicoDjango !== 'undefined' && nuevosDinamicoDjango.length > 0) {
        crearTarjetas(nuevosDinamicoDjango, "contenedor-dinamico", currentSlug);
    }
}