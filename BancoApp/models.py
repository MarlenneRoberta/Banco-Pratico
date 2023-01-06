from django.conf import settings
from django.db import models
from django.utils import timezone

class Cliente(models.Model):
    login = models.CharField(max_length= 11)
    senha = models.CharField(max_length=6)
    criar_data = models.DateTimeField(default = timezone.now)
    mostrar_data = models.DateTimeField(blank=True, null=True)

    def mostrar(self):
        self.mostrar_data = timezone.now()
        self.save()

    def __str__(self):
        return self.login

Class conta(models.Model):
    def __init__(self, valor_total_conta, ultima_atualizacao, numero_conta):
        self.valor_total_conta = saldo_atual
        self.ultima_atualizacao = saldo_atual - transferencia
        self.numero_da_conta = conta_destino

    def tensferencia_possivel(self, valor_total_conta, ):
        if valor_total_conta = 0.00:
            return ('Saldo insuficiente', self.valor_total_conta)
        else:
            return (self.realizar_transferencia)

    def realizar_transferencia (self, horario_transferencia, valor_taxa, valor_transferencia, taxa_extra):
        self.horario_transferencia = datetime.now()
        if horario_transferencia.hour >= datetime.time(9,00,0) & self.horario_transferencia.hour < datetime.time(18,00,0) && self.valor_transferencia <= 1000.00:
            self.valor_taxa = 5.00
            return (self.valor_transferencia + self.valor_taxa)
        else if self.horario_transferencia.hour < datetime.time(9,00,0). | self.horario_transferencia.hour >= datetime.time(18,00,0) && self.valor_transferencia <= 1000.00:
            self.valor_taxa = 7.00
            return (self.valor_transferencia + self.valor_taxa)
        else if self.valor_transferencia > 1000.00:
            self.taxa_extra = 10.00
            return (self.valor_taxa + self.valor_transferencia + self.taxa_extra)
