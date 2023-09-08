from django.http import HttpResponse
from django.shortcuts import render
from .models import Empleado, ProductosNuevos, ProductosUsados, Equipamiento
from .forms import EmpleadoFormulario, ProductosNuevosFormulario, ProductosUsadosFormulario, EquipamientosFormulario

# Create your views here.

def empleado(req, nombre, apellido, email, celular):
    
    empleado = Empleado(nombre=nombre, apellido=apellido, email=email, celular=celular)
    empleado.save()
    
    return HttpResponse(f"""
                        <p>Empleado: {empleado.nombre} {empleado.apellido} agregado!</p>
    """)

def productos_nuevos(req, marca, version, largo):
    
    productos_nuevos = ProductosNuevos(marca=marca, version=version, largo=largo)
    productos_nuevos.save()
    
def productos_usados(req, marca, version, largo):
    
    productos_usados = ProductosUsados(marca=marca, version=version, largo=largo)
    productos_usados.save()
    
def equipamiento(req, Nombre, descripcion):
    
    equipamiento = Equipamiento(Nombre=Nombre, descripcion=descripcion)
    equipamiento.save()
    
def lista_empleados(req):
    
    lista = Empleado.objects.all()
    
    return render(req, "lista_empleados.html", {"lista_empleados": lista})

def inicio(req):
    
    return render(req, "inicio.html")

def empleado(req):
    
    return render(req, "empleado.html")

def productos_nuevos(req):
    
    return render(req, "productos_nuevos.html")

def productos_usados(req):
    
    return render(req, "productos_usados.html")
                        
def equipamiento(req):
    
    return render(req, "equipamiento.html")

def empleado_formulario(req):
    
    print('method', req.method)
    print('post', req.POST)
    
    if req.method == 'POST' :
        
        miformulario = EmpleadoFormulario(req.POST)
        
        if miformulario.is_valid():
            
            print(miformulario.cleaned_data)
            data = miformulario.cleaned_data
            
            empleado = Empleado(nombre=data["nombre"], apellido=data["apellido"], email=data["email"], celular=data["celular"])
            empleado.save()
            return render(req, "inicio.html", {"mensaje": "Se ah generado un nuevo empleado con éxito"})
        else:
            return render(req, "inicio.html", {"mensaje": "Formulario inválido"})
    else:
        
        miformulario = EmpleadoFormulario()
        
        return render(req, "empleado_formulario.html", {"miformulario": miformulario})
    
def productosnuevos_formulario(req):
    
    print('method', req.method)
    print('post', req.POST)
    
    if req.method == 'POST' :
        
        miformulario = ProductosNuevosFormulario(req.POST)
        
        if miformulario.is_valid():
            
            print(miformulario.cleaned_data)
            data = miformulario.cleaned_data
            
            productos_nuevos = ProductosNuevos(marca=data["marca"], version=data["version"], largo=data["largo"])
            productos_nuevos.save()
            
            return render(req, "inicio.html", {"mensaje": "Se ah generado un nuevo producto 0Km"})
        else:
            return render(req, "inicio.html", {"mensaje": "Formulario inválido"})
    else:
        
        miformulario = ProductosNuevosFormulario()
        
        return render(req, "productosnuevos_formulario.html", {"miformulario": miformulario})

def productosusados_formulario(req):
    
    print('method', req.method)
    print('post', req.POST)
    
    if req.method == 'POST' :
        
        miformulario = ProductosUsadosFormulario(req.POST)
        
        if miformulario.is_valid():
            
            print(miformulario.cleaned_data)
            data = miformulario.cleaned_data
            
            productos_usados = ProductosUsados(marca=data["marca"], version=data["version"], largo=data["largo"])
            productos_usados.save()
            
            return render(req, "inicio.html", {"mensaje": "Se ah generado un nuevo producto usado"})
        else:
            return render(req, "inicio.html", {"mensaje": "Formulario inválido"})
    else:
        
        miformulario = ProductosUsadosFormulario()
        
        return render(req, "productosusados_formulario.html", {"miformulario": miformulario})

def equipamientos_formulario(req):
    
    print('method', req.method)
    print('post', req.POST)
    
    if req.method == 'POST' :
        
        miformulario = EquipamientosFormulario(req.POST)
        
        if miformulario.is_valid():
            
            print(miformulario.cleaned_data)
            data = miformulario.cleaned_data
            
            equipamiento = Equipamiento(Nombre=data["Nombre"], descripcion=data["descripcion"])
            equipamiento.save()
            
            return render(req, "inicio.html", {"mensaje": "Se ah generado un nuevo producto de equipamiento"})
        else:
            return render(req, "inicio.html", {"mensaje": "Formulario inválido"})
    else:
        
        miformulario = EquipamientosFormulario()
        
        return render(req, "equipamientos_formulario.html", {"miformulario": miformulario})
    

def busqueda_apellido(req):
    
    return render(req, 'busqueda_apellido.html')

def buscar(req):
    
    if req.GET["apellido"]:
        apellido = req.GET["apellido"]
        empleado = Empleado.objects.get(apellido=apellido)
        if empleado:
            return render(req, "resultadoBusqueda.html", {"empleado": empleado})
    else:
        return HttpResponse('No escribiste ningún apellido')