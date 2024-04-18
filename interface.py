import tkinter as tk
from tkinter import *
import customtkinter as ctk
from pathlib import Path
import criarfilhos as cf
from CTkScrollableDropdown import *



def acao(vetor_individuos1):
  vetor_individuos1 = cf.atualizar_individuos(len(vetor_individuos1), vetor_individuos1)
  print("dsad")

def stringnumerica(text):
  if text != "" and text != "0":
    try:
      float(text)
    except ValueError:
      return 2
    return 1 #se a string for numerica
  else:
    return 3 #string vazia ou zero

def stringnumerica2(text):
  if text != "" and text != "0":
    try:
      float(text)
    except ValueError:
      return 2
    if float(text) > 10 or float(text) < -10:
      return 3
    return 1 #se a string for numerica
  else:
    return 3 #string vazia ou zero


def max_gen_att(varname, index, mode):
  if var_max_gen.get():
    txt_informe.place(relx=0.15, rely=0.32, anchor=CENTER)
    ent_maxgen.place(relx=0.3, rely=0.32, anchor=CENTER)
    erro_maxgen(0,0,0)
  else:
    txt_informe.place_forget()
    ent_maxgen.place_forget()
    txt_erro_maxgen.place_forget()
    var_ent_maxgen.set("150")
    txt_erro_maxgen_zero.place_forget()
    botao_inicio_teste()

def goal_att(varname, index, mode):
  if var_valor_goal.get():
    txt_informegoal.place(relx=0.42, rely=0.32, anchor=CENTER)
    ent_goal.place(relx=0.515, rely=0.32, anchor=CENTER)
    erro_goal(0,0,0)
  else:
    txt_informegoal.place_forget()
    ent_goal.place_forget()
    txt_erro_goal.place_forget()
    var_ent_goal.set("")
    txt_erro_goal_zero.place_forget()
    botao_inicio_teste()

def conver_att(varname, index, mode):
  if var_convergencia.get():
    txt_informeconver.place(relx=0.65, rely=0.32, anchor=CENTER)
    ent_conver.place(relx=0.773, rely=0.32, anchor=CENTER)
    var_ent_conver.set("25")
    erro_conver(0,0,0)
  else:
    txt_informeconver.place_forget()
    ent_conver.place_forget()
    txt_erro_conver.place_forget()
    var_ent_conver.set("")
    txt_erro_conver_zero.place_forget()
    botao_inicio_teste()



def erro_maxgen(varname, index, mode):
  if stringnumerica(var_ent_maxgen.get()) == 1:
    txt_erro_maxgen.place_forget()
    txt_erro_maxgen_zero.place_forget()
    botao_inicio_teste()
  if stringnumerica(var_ent_maxgen.get()) == 2:
    txt_erro_maxgen.place(relx=0.2, rely=0.375, anchor=CENTER)
    txt_erro_maxgen_zero.place_forget()
    botao_inicio_teste()
  if stringnumerica(var_ent_maxgen.get()) == 3:
    txt_erro_maxgen.place_forget()
    txt_erro_maxgen_zero.place(relx=0.2, rely=0.375, anchor=CENTER)
    botao_inicio_teste()

def erro_goal(varname, index, mode):
  if stringnumerica(var_ent_goal.get()) == 1:
    txt_erro_goal.place_forget()
    txt_erro_goal_zero.place_forget()
    botao_inicio_teste()
  if stringnumerica(var_ent_goal.get()) == 2:
    txt_erro_goal.place(relx=0.47, rely=0.375, anchor=CENTER)
    txt_erro_goal_zero.place_forget()
    botao_inicio_teste()
  if stringnumerica(var_ent_goal.get()) == 3:
    txt_erro_goal_zero.place(relx=0.47, rely=0.375, anchor=CENTER)
    txt_erro_goal.place_forget()
    botao_inicio_teste()

def erro_conver(varname, index, mode):
  if stringnumerica(var_ent_conver.get()) == 1:
    txt_erro_conver.place_forget()
    txt_erro_conver_zero.place_forget()
    botao_inicio_teste()
  if stringnumerica(var_ent_conver.get()) == 2:
    txt_erro_conver.place(relx=0.7, rely=0.375, anchor=CENTER)
    txt_erro_conver_zero.place_forget()
    botao_inicio_teste()
  if stringnumerica(var_ent_conver.get()) == 3:
    txt_erro_conver_zero.place(relx=0.7, rely=0.375, anchor=CENTER)
    txt_erro_conver.place_forget()
    botao_inicio_teste()

def erro_num_indiv(varname, index, mode):
  if stringnumerica(var_ent_num_indv.get()) == 1:
    txt_erro_num_indv.place_forget()
    txt_erro_num_indv_zero.place_forget()
    bttn_gerar_indv.configure(state="normal")
    botao_inicio_teste()
  if stringnumerica(var_ent_num_indv.get()) == 2:
    txt_erro_num_indv.place(relx=0.645, rely=0.26, anchor=CENTER)
    txt_erro_num_indv_zero.place_forget()
    bttn_gerar_indv.configure(state="disabled")
    botao_inicio_teste()
  if stringnumerica(var_ent_num_indv.get()) == 3:
    txt_erro_num_indv_zero.place(relx=0.645, rely=0.26, anchor=CENTER)
    txt_erro_num_indv.place_forget()
    bttn_gerar_indv.configure(state="disabled")
    botao_inicio_teste()

def erro_x_indv(varname, index, mode):
  vetor_individuos[individuo].set_x(var_ent_x.get())
  if stringnumerica2(var_ent_x.get()) == 1 or var_ent_x.get() == "0" or var_ent_x.get() == "randomico":
    txt_erro_ent_x.place_forget()
    txt_erro_ent_x_vazia.place_forget()
    botao_inicio_teste()
  elif stringnumerica2(var_ent_x.get()) == 2:
    txt_erro_ent_x.place(relx=0.35, rely=0.73, anchor=CENTER)
    txt_erro_ent_x_vazia.place_forget()
    botao_inicio_teste()
  elif stringnumerica2(var_ent_x.get()) == 3 and var_ent_x.get() != "0":
    txt_erro_ent_x_vazia.place(relx=0.35, rely=0.73, anchor=CENTER)
    txt_erro_ent_x.place_forget()
    botao_inicio_teste()

def erro_y_indv(varname, index, mode):
  vetor_individuos[individuo].set_y(var_ent_y.get())
  if stringnumerica2(var_ent_y.get()) == 1 or var_ent_y.get() == "0" or var_ent_y.get() == "randomico":
    txt_erro_ent_y.place_forget()
    txt_erro_ent_y_vazia.place_forget()
    botao_inicio_teste()
  elif stringnumerica2(var_ent_y.get()) == 2:
    txt_erro_ent_y.place(relx=0.35, rely=0.98, anchor=CENTER)
    txt_erro_ent_y_vazia.place_forget()
    botao_inicio_teste()
  elif stringnumerica2(var_ent_y.get()) == 3 and var_ent_y != "0":
    txt_erro_ent_y_vazia.place(relx=0.35, rely=0.98, anchor=CENTER)
    txt_erro_ent_y.place_forget()
    botao_inicio_teste()



def gerar_indv():
  ent_num_indv.configure(state="disabled", fg_color="#0c1a20", border_color="#204d53", text_color="grey")
  txt_num_indv.configure(text_color="grey")
  indv_nao_gerados.set("false")
  txt_indv_nao_gerados.place_forget()
  inteiro = int(var_ent_num_indv.get())

  global vetor_individuos 
  vetor_individuos = cf.criar_individuos(inteiro)
  global vetor_individuos_str
  vetor_individuos_str = cf.criar_vet_strings(inteiro)
  
  bttn_gerar_indv.place_forget()
  

  global optm_seletor_indv
  global var_seletor
  var_seletor = ctk.StringVar()
  var_seletor.set(vetor_individuos_str[0])
  optm_seletor_indv = ctk.CTkOptionMenu(janela,
                                        width=180,
                                        height=50,
                                        font=("Inter", 19, "bold"),
                                        variable=var_seletor,
                                        fg_color="#142C36",)
  optm_seletor_indv.place(relx=0.2, rely=0.67, anchor=CENTER)
  txt_exemplo_indv.place(relx=0.31, rely=0.85, anchor=CENTER)

  CTkScrollableDropdown(optm_seletor_indv,
                        values=vetor_individuos_str,
                        width=180,
                        height=200,
                        font=("Inter", 19, "bold"),)
  var_seletor.trace_add("write", troca_indv)
  troca_indv(0,0,0)
  botao_inicio_teste()

def botao_inicio_teste():
  string_n_numerica = False
  sem_criterio_parada = False
  var_zero = False
  erro_indv = False
  if stringnumerica(var_ent_maxgen.get()) == 2 or stringnumerica(var_ent_goal.get()) == 2 or stringnumerica(var_ent_conver.get()) == 2 or stringnumerica(var_ent_num_indv.get()) == 2:
    string_n_numerica = True

  if not(var_convergencia.get()) and not(var_valor_goal.get()) and not(var_max_gen.get()):
    sem_criterio_parada = True

  if (stringnumerica(var_ent_maxgen.get()) == 3 and var_max_gen.get() == True) or (stringnumerica(var_ent_goal.get()) == 3 and var_valor_goal.get() == True) or (stringnumerica(var_ent_conver.get()) == 3 and var_convergencia.get() == True) or stringnumerica(var_ent_num_indv.get()) == 3:
    var_zero = True

  if indv_nao_gerados.get() == "false":
    if   stringnumerica2(vetor_individuos[individuo].get_x()) == 2 and vetor_individuos[individuo].get_x() != "randomico":
      erro_indv = True
    elif stringnumerica2(vetor_individuos[individuo].get_x()) == 3 and vetor_individuos[individuo].get_x() != "0":
      erro_indv = True
    elif stringnumerica2(vetor_individuos[individuo].get_y()) == 2 and vetor_individuos[individuo].get_y() != "randomico":
      erro_indv = True
    elif stringnumerica2(vetor_individuos[individuo].get_y()) == 3 and vetor_individuos[individuo].get_y() != "0":
      erro_indv = True

  if (string_n_numerica or sem_criterio_parada or var_zero or indv_nao_gerados.get() == "true" or erro_indv):
    bttn_inicio.configure(state="disabled")
  else:
    bttn_inicio.configure(state="normal")

  if sem_criterio_parada:
    txt_erro_semcriterio.place(relx=0.85, rely=0.11, anchor=CENTER)
  else:
    txt_erro_semcriterio.place_forget()
  
  if indv_nao_gerados.get() == "false":
    if erro_indv:
      optm_seletor_indv.configure(state="disabled")
    else:
      optm_seletor_indv.configure(state="normal")

def troca_indv(varname, index, mode):
  global individuo
  individuo = var_seletor.get()
  individuo = int(individuo[10:len(individuo)])
  individuo = individuo - 1
  
  global var_ent_x
  var_ent_x = ctk.StringVar()
  var_ent_x.set(vetor_individuos[individuo].get_x())
  ent_x_indv = ctk.CTkEntry(master=janela,
                          placeholder_text="1, 2, 3...",
                          fg_color="#142C36",
                          border_color="#29636B",
                          font=("Inter", 22, "bold"),
                          placeholder_text_color="#646464",
                          text_color="white",
                          width=300,
                          height=50,
                          textvariable=var_ent_x)
  ent_x_indv.place(relx=0.35, rely=0.78, anchor=CENTER)
  txt_x_indv = ctk.CTkLabel(master=janela,
                            text="X:",
                            text_color="white",
                            font=("Inter", 22, "bold"))
  txt_x_indv.place(relx=0.16, rely=0.78, anchor=CENTER)
  var_ent_x.trace_add("write", erro_x_indv)

  global var_ent_y
  var_ent_y = ctk.StringVar()
  var_ent_y.set(vetor_individuos[individuo].get_y())
  ent_y_indv = ctk.CTkEntry(master=janela,
                          placeholder_text="1, 2, 3...",
                          fg_color="#142C36",
                          border_color="#29636B",
                          font=("Inter", 22, "bold"),
                          placeholder_text_color="#646464",
                          text_color="white",
                          width=300,
                          height=50,
                          textvariable=var_ent_y)
  ent_y_indv.place(relx=0.35, rely=0.92, anchor=CENTER)
  txt_y_indv = ctk.CTkLabel(master=janela,
                            text="Y:",
                            text_color="white",
                            font=("Inter", 22, "bold"))
  txt_y_indv.place(relx=0.16, rely=0.92, anchor=CENTER)
  var_ent_y.trace_add("write", erro_y_indv)







janela = ctk.CTk()

#configurações da janela
corfundo = "#242424"
janela.title("Algoritmo Genetico Equipe 2")
janela.configure()
janela.geometry("900x700")
janela.resizable(False, False)
caminho_imagem = Path(__file__).parent / 'imagens' / 'dna_branco2.ico'
janela.iconbitmap(default=str(caminho_imagem))
ctk.set_appearance_mode("dark")
global vetor_individuos
vetor_individuos = cf.criar_individuos(1)
global individuo
individuo = 0






#texto alg genetico
txt_titulo = ctk.CTkLabel(master=janela,    
                      text="Algoritmo Genetico",
                      font=("Inter", 24, "bold"),
                      text_color="white")
txt_titulo.place(relx=0.5, rely=0.03, anchor=CENTER)



#texto criterio parada
txt_critP = ctk.CTkLabel(master=janela, 
                     text="Criterios de parada:",
                     font=("Inter", 19, "bold"), 
                     text_color="white")
txt_critP.place(relx=0.11, rely=0.07, anchor=CENTER)



#botão de inicio
bttn_inicio = ctk.CTkButton(master=janela,
                              text="Iniciar",
                              font=("Inter", 26, "bold"),
                              text_color="black",
                              width=128,
                              height=71,
                              corner_radius=15,
                              fg_color="#056B1B",
                              hover_color="#054E15",
                              command=lambda: acao(vetor_individuos),
                              state="disabled")
bttn_inicio.place(relx=0.85, rely=0.20, anchor=CENTER)



#checkbox1
var_max_gen = tk.BooleanVar()
chkb_check1 = ctk.CTkCheckBox(master=janela,
                              width=32,
                              height=32,
                              checkbox_width=32,
                              checkbox_height=32,
                              corner_radius=8,
                              fg_color="#142C36",
                              hover_color="#142C36",
                              border_color="#29636B",
                              variable=var_max_gen,
                              text="",
                              border_width=2)
chkb_check1.place(relx=0.085, rely=0.13, anchor=CENTER)
var_max_gen.trace_add("write",  max_gen_att)



#checkbox2
var_valor_goal = tk.BooleanVar()
chkb_check2 = ctk.CTkCheckBox(master=janela,
                              width=32,
                              height=32,
                              checkbox_width=32,
                              checkbox_height=32,
                              corner_radius=8,
                              fg_color="#142C36",
                              hover_color="#142C36",
                              border_color="#29636B",
                              variable=var_valor_goal,
                              text="",
                              border_width=2)
chkb_check2.place(relx=0.265, rely=0.13, anchor=CENTER)
var_valor_goal.trace_add("write",  goal_att)


#checkbox3 convergencia
var_convergencia = tk.BooleanVar()
var_convergencia.set(True)
chkb_check3 = ctk.CTkCheckBox(master=janela,
                              width=32,
                              height=32,
                              checkbox_width=32,
                              checkbox_height=32,
                              corner_radius=8,
                              fg_color="#142C36",
                              hover_color="#142C36",
                              border_color="#29636B",
                              variable=var_convergencia,
                              text="",
                              border_width=2,)
chkb_check3.place(relx=0.445, rely=0.13, anchor=CENTER)
var_convergencia.trace_add("write", conver_att)



#texto max gen
txt_maxgen = ctk.CTkLabel(master=janela, 
                     text="N° Max de Gerações",
                     font=("Inter", 19, "bold"), 
                     text_color="white",
                     wraplength=150)
txt_maxgen.place(relx=0.08, rely=0.2, anchor=CENTER)



#texto valor goal
txt_valorgoal = ctk.CTkLabel(master=janela, 
                     text="Valor Alcançado",
                     font=("Inter", 19, "bold"), 
                     text_color="white",
                     wraplength=100)
txt_valorgoal.place(relx=0.26, rely=0.2, anchor=CENTER)



#texto conver
txt_conver = ctk.CTkLabel(master=janela, 
                     text="Convergencia Prematura",
                     font=("Inter", 19, "bold"), 
                     text_color="white",
                     wraplength=150)
txt_conver.place(relx=0.44, rely=0.2, anchor=CENTER)



#texto que aparece quando marca a check max gen
txt_informe = ctk.CTkLabel(master=janela, 
                             text="Informe o número máximo de gerações:",
                             font=("Inter", 15, "bold"), 
                             text_color="white",
                             wraplength=170)



#entrada max gen
var_ent_maxgen = ctk.StringVar()
var_ent_maxgen.set("150")
ent_maxgen = ctk.CTkEntry(master=janela,
                          placeholder_text="1, 2, 3...",
                          fg_color="#142C36",
                          border_color="#29636B",
                          font=("Inter", 17, "bold"),
                          placeholder_text_color="#646464",
                          width=80,
                          height=40,
                          textvariable=var_ent_maxgen)
var_ent_maxgen.trace_add("write", erro_maxgen)



#texto que aparece quando marca a check goal
txt_informegoal = ctk.CTkLabel(master=janela, 
                             text="Informe o valor:",
                             font=("Inter", 15, "bold"), 
                             text_color="white",
                             wraplength=100)



#entrada valor
var_ent_goal = ctk.StringVar()
var_ent_goal.set("")
ent_goal = ctk.CTkEntry(master=janela,
                          placeholder_text="1, 2, 3...",
                          fg_color="#142C36",
                          border_color="#29636B",
                          font=("Inter", 17, "bold"),
                          placeholder_text_color="#646464",
                          width=80,
                          height=40,
                          textvariable=var_ent_goal)
var_ent_goal.trace_add("write", erro_goal)



#texto que aparece quando marca a check convergencia
txt_informeconver = ctk.CTkLabel(master=janela, 
                             text="Numero de interações para convergencia:",
                             font=("Inter", 13, "bold"), 
                             text_color="white",
                             wraplength=150)
txt_informeconver.place(relx=0.65, rely=0.32, anchor=CENTER)
    


#entrada conver
var_ent_conver = ctk.StringVar()
var_ent_conver.set("25")
ent_conver = ctk.CTkEntry(master=janela,
                          placeholder_text="1, 2, 3...",
                          fg_color="#142C36",
                          border_color="#29636B",
                          font=("Inter", 17, "bold"),
                          placeholder_text_color="#646464",
                          width=80,
                          height=40,
                          textvariable=var_ent_conver)
var_ent_conver.trace_add("write", erro_conver)
ent_conver.place(relx=0.773, rely=0.32, anchor=CENTER)



#texto erro maxgen
txt_erro_maxgen = ctk.CTkLabel(master=janela, 
                             text="Informe apenas numeros!",
                             font=("Inter", 12, "bold"), 
                             text_color="red",
                             wraplength=200)



#texto erro goal
txt_erro_goal = ctk.CTkLabel(master=janela, 
                             text="Informe apenas numeros!",
                             font=("Inter", 12, "bold"), 
                             text_color="red",
                             wraplength=200)




#texto erro convergencia
txt_erro_conver = ctk.CTkLabel(master=janela, 
                             text="Informe apenas numeros!",
                             font=("Inter", 12, "bold"), 
                             text_color="red",
                             wraplength=200)



#texto sem criterio de parada
txt_erro_semcriterio = ctk.CTkLabel(master=janela, 
                             text="Selecione ao menos um criterio de parada!",
                             font=("Inter", 12, "bold"), 
                             text_color="red",
                             wraplength=150)



#numero de individuos a serem criados
var_ent_num_indv = ctk.StringVar()
var_ent_num_indv.set("50")
ent_num_indv = ctk.CTkEntry(master=janela,
                          placeholder_text="1, 2, 3...",
                          fg_color="#142C36",
                          border_color="#29636B",
                          font=("Inter", 17, "bold"),
                          placeholder_text_color="#646464",
                          text_color="white",
                          width=80,
                          height=40,
                          textvariable=var_ent_num_indv)
var_ent_num_indv.trace_add("write", erro_num_indiv)
ent_num_indv.place(relx=0.645, rely=0.2, anchor=CENTER)



#texto sem criterio de parada
txt_erro_num_indv = ctk.CTkLabel(master=janela, 
                             text="Informe apenas numeros!",
                             font=("Inter", 12, "bold"), 
                             text_color="red",
                             wraplength=150)



#texto que aparece quando marca a check max gen
txt_num_indv = ctk.CTkLabel(master=janela, 
                             text="N° de individuos por geração:",
                             font=("Inter", 19, "bold"), 
                             text_color="white",
                             wraplength=160)
txt_num_indv.place(relx=0.645, rely=0.13, anchor=CENTER)



#texto maxgen = 0
txt_erro_maxgen_zero = ctk.CTkLabel(master=janela, 
                             text="O numero não pode ser zero!",
                             font=("Inter", 12, "bold"), 
                             text_color="red",
                             wraplength=150)



#texto valor goal = 0
txt_erro_goal_zero = ctk.CTkLabel(master=janela, 
                             text="O numero não pode ser zero!",
                             font=("Inter", 12, "bold"), 
                             text_color="red",
                             wraplength=150)



#texto conver = 0
txt_erro_conver_zero = ctk.CTkLabel(master=janela, 
                             text="O numero não pode ser zero!",
                             font=("Inter", 12, "bold"), 
                             text_color="red",
                             wraplength=150)



#texto num indv = 0
txt_erro_num_indv_zero = ctk.CTkLabel(master=janela, 
                             text="O numero não pode ser zero!",
                             font=("Inter", 12, "bold"), 
                             text_color="red",
                             wraplength=150)



#botão gerar individuos
indv_nao_gerados = ctk.StringVar()
indv_nao_gerados.set("true")
bttn_gerar_indv = ctk.CTkButton(master=janela,
                              text="Gerar Individuos",
                              font=("Inter", 26, "bold"),
                              text_color="black",
                              width=128,
                              height=71,
                              corner_radius=15,
                              fg_color="#e6c619",
                              hover_color="#b29a13",
                              command=gerar_indv)
bttn_gerar_indv.place(relx=0.25, rely=0.73, anchor=CENTER)



#texto individuos não gerados
txt_indv_nao_gerados = ctk.CTkLabel(master=janela, 
                             text="Gere os individuos primeiro",
                             font=("Inter", 12, "bold"), 
                             text_color="#e6c619",
                             wraplength=150,
                             width= 200)
txt_indv_nao_gerados.place(relx=0.85, rely=0.11, anchor=CENTER)



#texto erro se a entrada do x for não numerica
txt_erro_ent_x = ctk.CTkLabel(master=janela, 
                             text="Informe apenas numeros ou 'randomico'!",
                             font=("Inter", 12, "bold"), 
                             text_color="red",
                             wraplength=300)



#texto erro se a entrada do y for não numerica
txt_erro_ent_y = ctk.CTkLabel(master=janela, 
                             text="Informe apenas numeros ou 'randomico'!",
                             font=("Inter", 12, "bold"), 
                             text_color="red",
                             wraplength=300)



#texto erro se a entrada do x for vazia
txt_erro_ent_x_vazia = ctk.CTkLabel(master=janela, 
                             text="O valor não pode estar vazio e deve estar entre -10 e 10!",
                             font=("Inter", 12, "bold"), 
                             text_color="red",
                             wraplength=340)



#texto erro se a entrada do y for vazia
txt_erro_ent_y_vazia = ctk.CTkLabel(master=janela, 
                             text="O valor não pode estar vazio e deve estar entre -10 e 10!",
                             font=("Inter", 12, "bold"), 
                             text_color="red",
                             wraplength=340)



#texto exemplo entrada individuos
txt_exemplo_indv = ctk.CTkLabel(master=janela, 
                             text="Num: -3.1252 ou 'randomico'",
                             font=("Inter", 16, "bold"), 
                             text_color="white",
                             wraplength=340)

var_ent_porcentagem = ctk.StringVar()
var_ent_porcentagem.set("1")
ent_num_indv = ctk.CTkEntry(master=janela,
                          placeholder_text="1, 2, 3...",
                          fg_color="#142C36",
                          border_color="#29636B",
                          font=("Inter", 17, "bold"),
                          placeholder_text_color="#646464",
                          text_color="white",
                          width=80,
                          height=40,
                          textvariable=var_ent_num_indv)
var_ent_porcentagem.trace_add("write", erro_num_porcentagem)
ent_num_indv.place(relx=0.645, rely=0.2, anchor=CENTER)

#mandar para o veberson(CLASS individuos vetor_de_individuos,         #vetor de individuos criados 
#                       criteiro de parada: bool max_gerações,
#                       numero de max gerações: int num_max_gerações,
#                       criterio de parada: bool valor maximo a ser atingido,
#                       numero a ser alcançado:int num_max_gerações,
#                       bool max_gerações,
#                       int num_max_gerações,
#                       )
janela.mainloop()