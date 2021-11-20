from django.shortcuts import render
from spyne.decorator import rpc
from spyne.model.binary import File,ByteArray
from spyne.model.complex import ComplexModel
from spyne.service import ServiceBase
from spyne.model.primitive import Integer,String,UnsignedInteger,Decimal,Image,Date
from spyne import Array