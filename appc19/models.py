# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class C19Autoaval(models.Model):
    pk_c19_autoaval = models.BigAutoField(primary_key=True)
    nr_cpf = models.CharField(max_length=11)
    dt_avaliacao = models.DateField(blank=True, null=True)
    fl_febre = models.CharField(max_length=1, blank=True, null=True)
    fl_dorcabeca = models.CharField(max_length=1, blank=True, null=True)
    fl_secrecao = models.CharField(max_length=1, blank=True, null=True)
    fl_garganta = models.CharField(max_length=1, blank=True, null=True)
    fl_tosse = models.CharField(max_length=1, blank=True, null=True)
    fl_respirar = models.CharField(max_length=1, blank=True, null=True)
    fl_dorcorpo = models.CharField(max_length=1, blank=True, null=True)
    fl_diarreia = models.CharField(max_length=1, blank=True, null=True)
    fl_olfpaladar = models.CharField(max_length=1, blank=True, null=True)
    fl_14contato = models.CharField(max_length=1, blank=True, null=True)
    dt_criado = models.DateField(blank=True, null=True)
    dt_cancel = models.DateField(blank=True, null=True)
    id_criado = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    id_cancel = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'c19_autoaval'


class C19Cadastro(models.Model):
    pk_c19_cadastro = models.BigAutoField(primary_key=True)
    nr_cpf = models.CharField(max_length=11, blank=True, null=True)
    no_funcionario = models.CharField(max_length=100, blank=True, null=True)
    fl_sexo = models.CharField(max_length=1, blank=True, null=True)
    dt_nascimento = models.DateField(blank=True, null=True)
    nr_nit = models.CharField(max_length=11, blank=True, null=True)
    nr_cbo = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    nr_cep = models.CharField(max_length=8, blank=True, null=True)
    no_logradouro = models.CharField(max_length=140, blank=True, null=True)
    sg_uf = models.CharField(max_length=2, blank=True, null=True)
    nr_numero = models.CharField(max_length=8, blank=True, null=True)
    no_bairro = models.CharField(max_length=40, blank=True, null=True)
    no_cidade = models.CharField(max_length=40, blank=True, null=True)
    nr_celular = models.CharField(max_length=11, blank=True, null=True)
    no_email = models.CharField(max_length=140, blank=True, null=True)
    cd_codemp = models.CharField(max_length=5, blank=True, null=True)
    nr_matricula = models.CharField(max_length=8, blank=True, null=True)
    dt_criado = models.DateField(blank=True, null=True)
    dt_cancel = models.DateField(blank=True, null=True)
    id_criado = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    id_cancel = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'c19_cadastro'


class C19Teste(models.Model):
    pk_c19_teste = models.BigAutoField(primary_key=True)
    dt_coleta = models.DateField(blank=True, null=True)
    dt_resultado = models.DateField(blank=True, null=True)
    dt_sintomas = models.DateField(blank=True, null=True)
    fl_resultado = models.CharField(max_length=1, blank=True, null=True)
    fl_febre = models.CharField(max_length=1, blank=True, null=True)
    fl_dorcabeca = models.CharField(max_length=1, blank=True, null=True)
    fl_secrecao = models.CharField(max_length=1, blank=True, null=True)
    nr_cpf = models.CharField(max_length=11, blank=True, null=True)
    fl_garganta = models.CharField(max_length=1, blank=True, null=True)
    fl_tosse = models.CharField(max_length=1, blank=True, null=True)
    fl_respirar = models.CharField(max_length=1, blank=True, null=True)
    fl_dorcorpo = models.CharField(max_length=1, blank=True, null=True)
    fl_diarreia = models.CharField(max_length=1, blank=True, null=True)
    fl_olfpaladar = models.CharField(max_length=1, blank=True, null=True)
    fl_14contato = models.CharField(max_length=1, blank=True, null=True)
    fl_diabetes = models.CharField(max_length=1, blank=True, null=True)
    fl_hipertensao = models.CharField(max_length=1, blank=True, null=True)
    fl_renal = models.CharField(max_length=1, blank=True, null=True)
    fl_resgrave = models.CharField(max_length=1, blank=True, null=True)
    dt_criado = models.DateField(blank=True, null=True)
    dt_cancel = models.DateField(blank=True, null=True)
    id_criado = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    id_cancel = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'c19_teste'
