from django import datetime
from django.db import models

class Cliente(models.Model):
    login = models.CharField(max_length= 11)
    senha = models.CharField(max_length=6)
    def mostrar_data(self, mostrar_data):
        self.mostrar_data = datetime.now()
        self.save()

    def __str__(self):
        return self.login

class Conta(models.Model):
    def __init__(self, valor_total_conta, ultima_atualizacao, numero_conta):
        self.valor_total_conta = self.saldo_atual
        self.ultima_atualizacao = (self.saldo_atual - self.transferencia_possivel)
        self.numero_da_conta = self.conta_destino

    def realizar_transferencia (self, horario_transferencia_realizada, valor_taxa, valor_transferencia_realizada, taxa_extra):
        self.horario_transferencia_realizada = datetime.now()
        if horario_transferencia_realizada.hour >= datetime.time(9,00,0) & self.horario_transferencia_realizada.hour < datetime.time(18,00,0) & self.valor_transferencia_realizada <= 1000.00:
            self.valor_taxa = 5.00
            return (self.valor_transferencia + self.valor_taxa)
        elif self.horario_transferencia_realizada.hour < datetime.time(9,00,0) | self.horario_transferencia_realizada.hour >= datetime.time(18,00,0) & self.valor_transferencia_realizada <= 1000.00:
            self.valor_taxa = 7.00
            return (self.valor_transferencia_realizada + self.valor_taxa)
        elif self.valor_transferencia_realizada > 1000.00:
            self.taxa_extra = 10.00
            return (self.valor_taxa + self.valor_transferencia_realizada + self.taxa_extra)

    def tensferencia_possivel(self, valor_total_conta, realizar_transferencia):
        self.valor_total_conta = valor_total_conta
        
        if (valor_total_conta < (self.valor_transferencia + self.valor_taxa)) :
            return ('Saldo insuficiente', self.valor_total_conta)
        else:
            return (self.realizar_transferencia)