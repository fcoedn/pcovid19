from django import forms
from .models import C19Cadastro, C19Teste, C19Autoaval


class MenuForm(forms.ModelForm):
      pass

class C19CadastroForm(forms.ModelForm):
      class Meta:
            model = C19Cadastro
            fields = ('nr_cpf','no_funcionario','fl_sexo','dt_nascimento','nr_nit','nr_cbo','nr_cep','no_logradouro',
                      'sg_uf','nr_numero','no_bairro','no_cidade','no_email','cd_codemp','nr_matricula')


class C19TesteForm(forms.ModelForm):
      class Meta:
            model = C19Teste
            fields = ('nr_cpf','dt_coleta','dt_resultado','dt_sintomas','fl_resultado','fl_febre','fl_dorcabeca',
                      'fl_secrecao','fl_garganta','fl_tosse','fl_respirar','fl_dorcorpo','fl_diarreia','fl_olfpaladar',
                      'fl_14contato','fl_diabetes','fl_hipertensao','fl_renal','fl_resgrave')


class C19AutoAvalForm(forms.ModelForm):
      class Meta:
            model = C19Autoaval
            fields = ('nr_cpf','dt_avaliacao','fl_febre','fl_dorcabeca','fl_secrecao','fl_garganta','fl_tosse',
                      'fl_respirar','fl_dorcorpo','fl_diarreia','fl_olfpaladar','fl_14contato')