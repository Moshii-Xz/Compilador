
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftCONCATleftMASMENOSleftPORDIVIDIDOleftPOTENCIAMODULOrightUMENOSBINARY CADENA CONCAT DECIMAL DISPLAY DIVIDIDO DUPOINT ENTERO FALSE GO ID IGUAL IGUALQUE IN INVALID LLAVDER LLAVIZQ MAS MAYIGU MAYQUE MENIGU MENOS MENQUE MODULO NIGUALQUE NUMBER PARDER PARIZQ POR POTENCIA PTCOMA REPEAT TEXT TRUE UNDER VALIDinit            : instruccionesinstrucciones    : instrucciones instruccioninstrucciones    : instruccion instruccion      : display_instr\n                        | definicion_instr\n                        | asignacion_instr\n                        | under_instr\n                        | valid_instr\n                        | invalid_instr\n                        | repeat_instr\n                        | go_under_instr display_instr     :  DISPLAY PARIZQ expresion_cadena PARDER PTCOMAtipo_dato : NUMBER\n                 | TEXT\n                 | BINARYdefinicion_instr : tipo_dato ID PTCOMA asignacion_instr   :  ID IGUAL expresion_numerica PTCOMA\n                          |  ID IGUAL expresion_cadena   PTCOMA \n                          |  ID IGUAL expresion_booleana PTCOMAunder_instr     : UNDER DUPOINT  expresion_comparativa  LLAVIZQ instrucciones LLAVDERgo_under_instr     : GO LLAVIZQ  instrucciones  LLAVDER UNDER  expresion_comparativa PTCOMA valid_instr  : VALID DUPOINT expresion_comparativa  LLAVIZQ instrucciones LLAVDERinvalid_instr      : VALID DUPOINT expresion_comparativa  LLAVIZQ instrucciones LLAVDER INVALID LLAVIZQ instrucciones LLAVDERrepeat_instr     : REPEAT DUPOINT ID PTCOMA expresion_comparativa IN expresion_numerica LLAVIZQ instrucciones LLAVDER expresion_numerica : expresion_numerica MAS expresion_numerica\n                          | expresion_numerica MENOS expresion_numerica\n                          | expresion_numerica POR expresion_numerica\n                          | expresion_numerica DIVIDIDO expresion_numerica\n                          | expresion_numerica MODULO expresion_numerica\n                          | expresion_numerica POTENCIA expresion_numerica expresion_numerica : MENOS expresion_numerica %prec UMENOSexpresion_numerica : PARIZQ expresion_numerica PARDERexpresion_numerica : ENTERO\n                          | DECIMALexpresion_numerica   : IDexpresion_cadena     : expresion_cadena CONCAT expresion_cadenaexpresion_cadena     : CADENAexpresion_cadena     : expresion_numericaexpresion_booleana : TRUE\n                          | FALSEexpresion_comparativa : expresion_numerica MAYQUE expresion_numerica\n                             | expresion_numerica MENQUE expresion_numerica\n                             | expresion_numerica IGUALQUE expresion_numerica\n                             | expresion_numerica MAYIGU expresion_numerica\n                             | expresion_numerica MENIGU expresion_numerica\n                             | expresion_numerica NIGUALQUE expresion_numerica'
    
_lr_action_items = {'DISPLAY':([0,2,3,4,5,6,7,8,9,10,11,22,29,38,48,59,60,61,62,69,73,81,88,91,92,97,98,99,100,101,102,103,],[12,12,-3,-4,-5,-6,-7,-8,-9,-10,-11,-2,12,-16,12,-17,-18,-19,12,12,-12,12,12,-20,-22,-21,12,12,12,12,-23,-24,]),'ID':([0,2,3,4,5,6,7,8,9,10,11,13,19,20,21,22,23,25,26,27,28,29,30,34,38,48,51,52,53,54,55,56,57,59,60,61,62,63,64,65,66,67,68,69,70,73,81,88,90,91,92,93,97,98,99,100,101,102,103,],[14,14,-3,-4,-5,-6,-7,-8,-9,-10,-11,24,-13,-14,-15,-2,37,37,37,37,47,14,37,37,-16,14,37,37,37,37,37,37,37,-17,-18,-19,14,37,37,37,37,37,37,14,37,-12,14,14,37,-20,-22,37,-21,14,14,14,14,-23,-24,]),'UNDER':([0,2,3,4,5,6,7,8,9,10,11,22,29,38,48,59,60,61,62,69,71,73,81,88,91,92,97,98,99,100,101,102,103,],[15,15,-3,-4,-5,-6,-7,-8,-9,-10,-11,-2,15,-16,15,-17,-18,-19,15,15,90,-12,15,15,-20,-22,-21,15,15,15,15,-23,-24,]),'VALID':([0,2,3,4,5,6,7,8,9,10,11,22,29,38,48,59,60,61,62,69,73,81,88,91,92,97,98,99,100,101,102,103,],[16,16,-3,-4,-5,-6,-7,-8,-9,-10,-11,-2,16,-16,16,-17,-18,-19,16,16,-12,16,16,-20,-22,-21,16,16,16,16,-23,-24,]),'REPEAT':([0,2,3,4,5,6,7,8,9,10,11,22,29,38,48,59,60,61,62,69,73,81,88,91,92,97,98,99,100,101,102,103,],[17,17,-3,-4,-5,-6,-7,-8,-9,-10,-11,-2,17,-16,17,-17,-18,-19,17,17,-12,17,17,-20,-22,-21,17,17,17,17,-23,-24,]),'GO':([0,2,3,4,5,6,7,8,9,10,11,22,29,38,48,59,60,61,62,69,73,81,88,91,92,97,98,99,100,101,102,103,],[18,18,-3,-4,-5,-6,-7,-8,-9,-10,-11,-2,18,-16,18,-17,-18,-19,18,18,-12,18,18,-20,-22,-21,18,18,18,18,-23,-24,]),'NUMBER':([0,2,3,4,5,6,7,8,9,10,11,22,29,38,48,59,60,61,62,69,73,81,88,91,92,97,98,99,100,101,102,103,],[19,19,-3,-4,-5,-6,-7,-8,-9,-10,-11,-2,19,-16,19,-17,-18,-19,19,19,-12,19,19,-20,-22,-21,19,19,19,19,-23,-24,]),'TEXT':([0,2,3,4,5,6,7,8,9,10,11,22,29,38,48,59,60,61,62,69,73,81,88,91,92,97,98,99,100,101,102,103,],[20,20,-3,-4,-5,-6,-7,-8,-9,-10,-11,-2,20,-16,20,-17,-18,-19,20,20,-12,20,20,-20,-22,-21,20,20,20,20,-23,-24,]),'BINARY':([0,2,3,4,5,6,7,8,9,10,11,22,29,38,48,59,60,61,62,69,73,81,88,91,92,97,98,99,100,101,102,103,],[21,21,-3,-4,-5,-6,-7,-8,-9,-10,-11,-2,21,-16,21,-17,-18,-19,21,21,-12,21,21,-20,-22,-21,21,21,21,21,-23,-24,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,22,38,59,60,61,73,91,92,97,102,103,],[0,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-2,-16,-17,-18,-19,-12,-20,-22,-21,-23,-24,]),'LLAVDER':([3,4,5,6,7,8,9,10,11,22,38,48,59,60,61,73,81,88,91,92,97,100,101,102,103,],[-3,-4,-5,-6,-7,-8,-9,-10,-11,-2,-16,71,-17,-18,-19,-12,91,92,-20,-22,-21,102,103,-23,-24,]),'PARIZQ':([12,23,25,26,27,30,34,51,52,53,54,55,56,57,63,64,65,66,67,68,70,90,93,],[23,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'IGUAL':([14,],[25,]),'DUPOINT':([15,16,17,],[26,27,28,]),'LLAVIZQ':([18,35,36,37,44,46,58,72,75,76,77,78,79,80,82,83,84,85,86,87,95,96,],[29,-33,-34,-35,62,69,-31,-32,-25,-26,-27,-28,-29,-30,-41,-42,-43,-44,-45,-46,98,99,]),'CADENA':([23,25,51,],[32,32,32,]),'MENOS':([23,25,26,27,30,33,34,35,36,37,39,45,49,51,52,53,54,55,56,57,58,63,64,65,66,67,68,70,72,75,76,77,78,79,80,82,83,84,85,86,87,90,93,96,],[34,34,34,34,34,53,34,-33,-34,-35,53,53,53,34,34,34,34,34,34,34,-31,34,34,34,34,34,34,34,-32,-25,-26,-27,-28,-29,-30,53,53,53,53,53,53,34,34,53,]),'ENTERO':([23,25,26,27,30,34,51,52,53,54,55,56,57,63,64,65,66,67,68,70,90,93,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'DECIMAL':([23,25,26,27,30,34,51,52,53,54,55,56,57,63,64,65,66,67,68,70,90,93,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'PTCOMA':([24,32,33,35,36,37,39,40,41,42,43,47,50,58,72,74,75,76,77,78,79,80,82,83,84,85,86,87,94,],[38,-37,-38,-33,-34,-35,59,60,61,-39,-40,70,73,-31,-32,-36,-25,-26,-27,-28,-29,-30,-41,-42,-43,-44,-45,-46,97,]),'TRUE':([25,],[42,]),'FALSE':([25,],[43,]),'PARDER':([31,32,33,35,36,37,49,58,72,74,75,76,77,78,79,80,],[50,-37,-38,-33,-34,-35,72,-31,-32,-36,-25,-26,-27,-28,-29,-30,]),'CONCAT':([31,32,33,35,36,37,39,40,58,72,74,75,76,77,78,79,80,],[51,-37,-38,-33,-34,-35,-38,51,-31,-32,-36,-25,-26,-27,-28,-29,-30,]),'MAS':([33,35,36,37,39,45,49,58,72,75,76,77,78,79,80,82,83,84,85,86,87,96,],[52,-33,-34,-35,52,52,52,-31,-32,-25,-26,-27,-28,-29,-30,52,52,52,52,52,52,52,]),'POR':([33,35,36,37,39,45,49,58,72,75,76,77,78,79,80,82,83,84,85,86,87,96,],[54,-33,-34,-35,54,54,54,-31,-32,54,54,-27,-28,-29,-30,54,54,54,54,54,54,54,]),'DIVIDIDO':([33,35,36,37,39,45,49,58,72,75,76,77,78,79,80,82,83,84,85,86,87,96,],[55,-33,-34,-35,55,55,55,-31,-32,55,55,-27,-28,-29,-30,55,55,55,55,55,55,55,]),'MODULO':([33,35,36,37,39,45,49,58,72,75,76,77,78,79,80,82,83,84,85,86,87,96,],[56,-33,-34,-35,56,56,56,-31,-32,56,56,56,56,-29,-30,56,56,56,56,56,56,56,]),'POTENCIA':([33,35,36,37,39,45,49,58,72,75,76,77,78,79,80,82,83,84,85,86,87,96,],[57,-33,-34,-35,57,57,57,-31,-32,57,57,57,57,-29,-30,57,57,57,57,57,57,57,]),'MAYQUE':([35,36,37,45,58,72,75,76,77,78,79,80,],[-33,-34,-35,63,-31,-32,-25,-26,-27,-28,-29,-30,]),'MENQUE':([35,36,37,45,58,72,75,76,77,78,79,80,],[-33,-34,-35,64,-31,-32,-25,-26,-27,-28,-29,-30,]),'IGUALQUE':([35,36,37,45,58,72,75,76,77,78,79,80,],[-33,-34,-35,65,-31,-32,-25,-26,-27,-28,-29,-30,]),'MAYIGU':([35,36,37,45,58,72,75,76,77,78,79,80,],[-33,-34,-35,66,-31,-32,-25,-26,-27,-28,-29,-30,]),'MENIGU':([35,36,37,45,58,72,75,76,77,78,79,80,],[-33,-34,-35,67,-31,-32,-25,-26,-27,-28,-29,-30,]),'NIGUALQUE':([35,36,37,45,58,72,75,76,77,78,79,80,],[-33,-34,-35,68,-31,-32,-25,-26,-27,-28,-29,-30,]),'IN':([35,36,37,58,72,75,76,77,78,79,80,82,83,84,85,86,87,89,],[-33,-34,-35,-31,-32,-25,-26,-27,-28,-29,-30,-41,-42,-43,-44,-45,-46,93,]),'INVALID':([92,],[95,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'instrucciones':([0,29,62,69,98,99,],[2,48,81,88,100,101,]),'instruccion':([0,2,29,48,62,69,81,88,98,99,100,101,],[3,22,3,22,3,3,22,22,3,3,22,22,]),'display_instr':([0,2,29,48,62,69,81,88,98,99,100,101,],[4,4,4,4,4,4,4,4,4,4,4,4,]),'definicion_instr':([0,2,29,48,62,69,81,88,98,99,100,101,],[5,5,5,5,5,5,5,5,5,5,5,5,]),'asignacion_instr':([0,2,29,48,62,69,81,88,98,99,100,101,],[6,6,6,6,6,6,6,6,6,6,6,6,]),'under_instr':([0,2,29,48,62,69,81,88,98,99,100,101,],[7,7,7,7,7,7,7,7,7,7,7,7,]),'valid_instr':([0,2,29,48,62,69,81,88,98,99,100,101,],[8,8,8,8,8,8,8,8,8,8,8,8,]),'invalid_instr':([0,2,29,48,62,69,81,88,98,99,100,101,],[9,9,9,9,9,9,9,9,9,9,9,9,]),'repeat_instr':([0,2,29,48,62,69,81,88,98,99,100,101,],[10,10,10,10,10,10,10,10,10,10,10,10,]),'go_under_instr':([0,2,29,48,62,69,81,88,98,99,100,101,],[11,11,11,11,11,11,11,11,11,11,11,11,]),'tipo_dato':([0,2,29,48,62,69,81,88,98,99,100,101,],[13,13,13,13,13,13,13,13,13,13,13,13,]),'expresion_cadena':([23,25,51,],[31,40,74,]),'expresion_numerica':([23,25,26,27,30,34,51,52,53,54,55,56,57,63,64,65,66,67,68,70,90,93,],[33,39,45,45,49,58,33,75,76,77,78,79,80,82,83,84,85,86,87,45,45,96,]),'expresion_booleana':([25,],[41,]),'expresion_comparativa':([26,27,70,90,],[44,46,89,94,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> instrucciones','init',1,'p_init','gramatica.py',142),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_lista','gramatica.py',147),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_instruccion','gramatica.py',153),
  ('instruccion -> display_instr','instruccion',1,'p_instruccion','gramatica.py',158),
  ('instruccion -> definicion_instr','instruccion',1,'p_instruccion','gramatica.py',159),
  ('instruccion -> asignacion_instr','instruccion',1,'p_instruccion','gramatica.py',160),
  ('instruccion -> under_instr','instruccion',1,'p_instruccion','gramatica.py',161),
  ('instruccion -> valid_instr','instruccion',1,'p_instruccion','gramatica.py',162),
  ('instruccion -> invalid_instr','instruccion',1,'p_instruccion','gramatica.py',163),
  ('instruccion -> repeat_instr','instruccion',1,'p_instruccion','gramatica.py',164),
  ('instruccion -> go_under_instr','instruccion',1,'p_instruccion','gramatica.py',165),
  ('display_instr -> DISPLAY PARIZQ expresion_cadena PARDER PTCOMA','display_instr',5,'p_instruccion_display','gramatica.py',169),
  ('tipo_dato -> NUMBER','tipo_dato',1,'p_tipo_dato','gramatica.py',173),
  ('tipo_dato -> TEXT','tipo_dato',1,'p_tipo_dato','gramatica.py',174),
  ('tipo_dato -> BINARY','tipo_dato',1,'p_tipo_dato','gramatica.py',175),
  ('definicion_instr -> tipo_dato ID PTCOMA','definicion_instr',3,'p_instruccion_definicion','gramatica.py',179),
  ('asignacion_instr -> ID IGUAL expresion_numerica PTCOMA','asignacion_instr',4,'p_asignacion_instr','gramatica.py',183),
  ('asignacion_instr -> ID IGUAL expresion_cadena PTCOMA','asignacion_instr',4,'p_asignacion_instr','gramatica.py',184),
  ('asignacion_instr -> ID IGUAL expresion_booleana PTCOMA','asignacion_instr',4,'p_asignacion_instr','gramatica.py',185),
  ('under_instr -> UNDER DUPOINT expresion_comparativa LLAVIZQ instrucciones LLAVDER','under_instr',6,'p_under_instr','gramatica.py',189),
  ('go_under_instr -> GO LLAVIZQ instrucciones LLAVDER UNDER expresion_comparativa PTCOMA','go_under_instr',7,'p_go_under_instr','gramatica.py',193),
  ('valid_instr -> VALID DUPOINT expresion_comparativa LLAVIZQ instrucciones LLAVDER','valid_instr',6,'p_valid_instr','gramatica.py',197),
  ('invalid_instr -> VALID DUPOINT expresion_comparativa LLAVIZQ instrucciones LLAVDER INVALID LLAVIZQ instrucciones LLAVDER','invalid_instr',10,'p_invalid_instr','gramatica.py',201),
  ('repeat_instr -> REPEAT DUPOINT ID PTCOMA expresion_comparativa IN expresion_numerica LLAVIZQ instrucciones LLAVDER','repeat_instr',10,'p_repeat_instr','gramatica.py',205),
  ('expresion_numerica -> expresion_numerica MAS expresion_numerica','expresion_numerica',3,'p_expresion_binaria','gramatica.py',209),
  ('expresion_numerica -> expresion_numerica MENOS expresion_numerica','expresion_numerica',3,'p_expresion_binaria','gramatica.py',210),
  ('expresion_numerica -> expresion_numerica POR expresion_numerica','expresion_numerica',3,'p_expresion_binaria','gramatica.py',211),
  ('expresion_numerica -> expresion_numerica DIVIDIDO expresion_numerica','expresion_numerica',3,'p_expresion_binaria','gramatica.py',212),
  ('expresion_numerica -> expresion_numerica MODULO expresion_numerica','expresion_numerica',3,'p_expresion_binaria','gramatica.py',213),
  ('expresion_numerica -> expresion_numerica POTENCIA expresion_numerica','expresion_numerica',3,'p_expresion_binaria','gramatica.py',214),
  ('expresion_numerica -> MENOS expresion_numerica','expresion_numerica',2,'p_expresion_unaria','gramatica.py',229),
  ('expresion_numerica -> PARIZQ expresion_numerica PARDER','expresion_numerica',3,'p_expresion_agrupacion','gramatica.py',234),
  ('expresion_numerica -> ENTERO','expresion_numerica',1,'p_expresion_number','gramatica.py',238),
  ('expresion_numerica -> DECIMAL','expresion_numerica',1,'p_expresion_number','gramatica.py',239),
  ('expresion_numerica -> ID','expresion_numerica',1,'p_expresion_id','gramatica.py',243),
  ('expresion_cadena -> expresion_cadena CONCAT expresion_cadena','expresion_cadena',3,'p_expresion_concatenacion','gramatica.py',247),
  ('expresion_cadena -> CADENA','expresion_cadena',1,'p_expresion_cadena','gramatica.py',251),
  ('expresion_cadena -> expresion_numerica','expresion_cadena',1,'p_expresion_cadena_numerico','gramatica.py',255),
  ('expresion_booleana -> TRUE','expresion_booleana',1,'p_expresion_booleana','gramatica.py',259),
  ('expresion_booleana -> FALSE','expresion_booleana',1,'p_expresion_booleana','gramatica.py',260),
  ('expresion_comparativa -> expresion_numerica MAYQUE expresion_numerica','expresion_comparativa',3,'p_expresion_comparativa','gramatica.py',264),
  ('expresion_comparativa -> expresion_numerica MENQUE expresion_numerica','expresion_comparativa',3,'p_expresion_comparativa','gramatica.py',265),
  ('expresion_comparativa -> expresion_numerica IGUALQUE expresion_numerica','expresion_comparativa',3,'p_expresion_comparativa','gramatica.py',266),
  ('expresion_comparativa -> expresion_numerica MAYIGU expresion_numerica','expresion_comparativa',3,'p_expresion_comparativa','gramatica.py',267),
  ('expresion_comparativa -> expresion_numerica MENIGU expresion_numerica','expresion_comparativa',3,'p_expresion_comparativa','gramatica.py',268),
  ('expresion_comparativa -> expresion_numerica NIGUALQUE expresion_numerica','expresion_comparativa',3,'p_expresion_comparativa','gramatica.py',269),
]
