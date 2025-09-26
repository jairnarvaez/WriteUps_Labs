# blog/scripts/populate_example.py
import sys
import os
import django

# Configurar Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WriteUps_Labs.settings")
django.setup()

from blog.models import Machine, Section, Step, StepBlock, Tag

# Limpiar datos existentes (opcional)
Machine.objects.all().delete()
Section.objects.all().delete()
Step.objects.all().delete()
StepBlock.objects.all().delete()
Tag.objects.all().delete()

# Crear etiquetas
tags = [Tag.objects.create(name=f"Tag{i}") for i in range(1, 4)]

# Crear máquinas y relaciones
for m_idx in range(1, 4):
    machine = Machine.objects.create(
        name=f"Machine {m_idx}",
        difficulty="Easy",
        summary=f"Resumen de la máquina {m_idx}"
    )
    machine.tags.set(tags[:m_idx])

    for s_idx in range(1, m_idx + 1):
        section = Section.objects.create(
            machine=machine,
            title=f"Sección {s_idx} de Machine {m_idx}",
            order=s_idx
        )

        for step_idx in range(1, 3):
            step = Step.objects.create(
                section=section,
                title=f"Paso {step_idx} de Sección {s_idx} de Machine {m_idx}",
                order=step_idx
            )

            for block_idx in range(1, 3):
                StepBlock.objects.create(
                    step=step,
                    type='description',
                    order=block_idx,
                    text=f"Texto del bloque {block_idx} del paso {step_idx}"
                )

print("Datos de ejemplo creados correctamente.")
