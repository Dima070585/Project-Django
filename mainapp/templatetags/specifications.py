from django import template
from django.utils.safestring import mark_safe

register = template.Library()


TABLE_HEAD = """
                <table class="table">
                  <tbody>
            """

TABLE_TAIL = """
                    </tbody>
                </table>
            """

TABLE_CONTENT = """
                <tr>
                    <td>{name}</td>                    
                    <td>{value}</td>                         
                </tr>
                """
PRODUCT_SPEC = {
    'sofa':{
        'Размеры (ДхГхВ)': 'size',
        'Наличие спального места': 'bed',
        'Размеры спального места (ДхГ)': 'bed_size',
        'Материал каркаса': 'frame_material',
        'Наполнение спального (посадочного) места': 'filling_the_bed',
        'Материал опор': 'support_material',
        'Материал обивки': 'upholstery_material',
        'Механизм трансформации': 'transformation_mechanism'
    },
    'chair':{
        'Размеры (ДхГхВ)': 'size',
        'Материал каркаса': 'frame_material',
        'Наполнение спального (посадочного) места': 'filling_the_bed',
        'Материал опор': 'support_material',
        'Материал обивки': 'upholstery_material'
    },
    'puf':{
        'Размеры (ДхГхВ)': 'size',
        'Материал каркаса': 'frame_material',
        'Наполнение спального (посадочного) места': 'filling_the_bed',
        'Материал опор': 'support_material',
        'Материал обивки': 'upholstery_material'
    },
    'bed':{
        'Размеры (ШхДхВ)': 'size',
        'Размеры спального места (ШхД)': 'bed_size',
        'Материал каркаса': 'frame_material',
        'Материал опор': 'support_material',
        'Материал обивки': 'upholstery_material'
    }
}

def get_product_spec(product, model_name):
    table_content = ''
    for name, value in PRODUCT_SPEC[model_name].items():

        if getattr(product, value) == True:
            table_content += TABLE_CONTENT.format(name=name, value='&#9989;')
        if getattr(product, value) == False:
            table_content += TABLE_CONTENT.format(name=name, value='&#10060;')
        if getattr(product, value) != True and getattr(product, value) != False:
            table_content += TABLE_CONTENT.format(name=name, value=getattr(product, value))
        print(getattr(product, value))
    return table_content

@register.filter
def product_spec(product):
    model_name = product.__class__._meta.model_name
    return mark_safe(TABLE_HEAD + get_product_spec(product, model_name) + TABLE_TAIL)