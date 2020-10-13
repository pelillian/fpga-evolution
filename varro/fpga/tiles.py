SIMPLE_STEP_TILES = [
    'CIB_R17C125:CIB_LR',
    'CIB_R13C125:CIB_LR',
    'CIB_R14C125:CIB_LR',
    'CIB_R15C125:CIB_LR',
    'CIB_R16C125:CIB_LR',
    'CIB_R18C125:CIB_LR',
    'CIB_R19C125:CIB_LR',
    'CIB_R20C125:CIB_LR',
    'CIB_R21C125:CIB_LR',
]

SIMPLE_STEP_OTHER_TILES = [
    'CIB_R10C3:PVT_COUNT2',
    'MIB_R10C126:BANKREF2',
    'MIB_R22C67:CMUX_UL_0',
    'MIB_R22C68:CMUX_UR_0',
    'MIB_R70C67:CMUX_LL_0',
    'MIB_R70C68:CMUX_LR_0',
    'MIB_R18C126:PICR1_DQS3',
    'MIB_R19C126:PICR2',
    'MIB_R38C126:PICR0',
    'MIB_R39C126:PICR1_DQS0',
    'MIB_R95C101:PICB0',
    'MIB_R95C102:PICB1',
    'MIB_R95C103:PICB0',
    'MIB_R95C104:PICB1',
    'MIB_R95C105:PICB0',
    'MIB_R95C106:PICB1',
    'MIB_R95C107:PICB0',
    'MIB_R95C108:PICB1',
    'MIB_R95C110:PICB0',
    'MIB_R95C111:PICB1',
    'MIB_R95C112:PICB0',
    'MIB_R95C113:PICB1',
    'MIB_R95C114:PICB0',
    'MIB_R95C115:PICB1',
    'MIB_R95C116:PICB0',
    'MIB_R95C117:PICB1',
    'MIB_R95C119:PICB0',
    'MIB_R95C120:PICB1',
    'MIB_R95C121:PICB0',
    'MIB_R95C122:PICB1',
    'MIB_R95C4:EFB0_PICB0',
    'MIB_R95C96:PICB0',
    'MIB_R95C97:PICB1',
    'MIB_R95C98:PICB0',
    'MIB_R95C99:PICB1'
]

SIMPLE_STEP_CFG = """
.tile CIB_R10C3:PVT_COUNT2
unknown: F2B0
unknown: F3B0
unknown: F5B0
unknown: F11B0
unknown: F13B0

.tile CIB_R22C125:CIB_LR_S
arc: N1_V01N0001 JQ5
arc: N3_V06N0303 JF5

.tile CIB_R23C125:CIB_LR
arc: N3_V06N0303 S3_V06N0303

.tile CIB_R29C125:CIB_LR
arc: H01W0000 JQ5
arc: N3_V06N0303 JF5

.tile CIB_R31C125:CIB_LR
arc: S1_V02S0601 S3_V06N0303

.tile CIB_R32C125:CIB_LR
arc: W1_H02W0501 S3_V06N0303
arc: W1_H02W0601 V02S0601

.tile CIB_R34C124:CIB_DSP
arc: N1_V02N0301 H02W0301

.tile CIB_R34C125:CIB_LR_S
arc: W1_H02W0301 V01N0101

.tile CIB_R35C125:CIB_LR
arc: H01W0100 JQ5
arc: N1_V01N0101 JF5
arc: W1_H02W0501 JF5

.tile CIB_R37C125:CIB_LR
arc: H01W0100 JQ5
arc: N3_V06N0303 JF5

.tile CIB_R38C125:CIB_LR
arc: N3_V06N0303 JF5

.tile CIB_R5C125:CIB_PLL1
enum: CIB.JA3MUX 0
enum: CIB.JB3MUX 0

.tile CIB_R5C1:CIB_PLL1
enum: CIB.JA3MUX 0
enum: CIB.JB3MUX 0

.tile CIB_R94C123:CIB_PLL3
enum: CIB.JA3MUX 0
enum: CIB.JB3MUX 0

.tile CIB_R94C3:CIB_PLL3
enum: CIB.JA3MUX 0
enum: CIB.JB3MUX 0

.tile CIB_R94C46:CIB_DCU0
unknown: F20B10
unknown: F21B10
unknown: F22B10
unknown: F23B10
unknown: F28B10
unknown: F29B10
unknown: F30B10
unknown: F31B10
unknown: F74B10
unknown: F75B10
unknown: F76B10
unknown: F77B10
unknown: F82B10
unknown: F83B10
unknown: F84B10
unknown: F85B10

.tile CIB_R94C47:CIB_DCUA
unknown: F20B10
unknown: F21B10
unknown: F22B10
unknown: F23B10
unknown: F28B10
unknown: F29B10
unknown: F30B10
unknown: F31B10
unknown: F74B10
unknown: F75B10
unknown: F76B10
unknown: F77B10
unknown: F82B10
unknown: F83B10
unknown: F84B10
unknown: F85B10

.tile CIB_R94C48:CIB_DCUB
unknown: F20B10
unknown: F21B10
unknown: F22B10
unknown: F23B10
unknown: F28B10
unknown: F29B10
unknown: F30B10
unknown: F31B10
unknown: F74B10
unknown: F75B10
unknown: F76B10
unknown: F77B10
unknown: F82B10
unknown: F83B10
unknown: F84B10
unknown: F85B10

.tile CIB_R94C49:CIB_DCUC
unknown: F20B10
unknown: F21B10
unknown: F22B10
unknown: F23B10
unknown: F28B10
unknown: F29B10
unknown: F30B10
unknown: F31B10
unknown: F74B10
unknown: F75B10
unknown: F76B10
unknown: F77B10
unknown: F82B10
unknown: F83B10
unknown: F84B10
unknown: F85B10

.tile CIB_R94C50:CIB_DCUD
unknown: F20B10
unknown: F21B10
unknown: F22B10
unknown: F23B10
unknown: F28B10
unknown: F29B10
unknown: F31B10
unknown: F74B10
unknown: F75B10
unknown: F76B10
unknown: F77B10
unknown: F82B10
unknown: F83B10
unknown: F84B10
unknown: F85B10

.tile CIB_R94C51:CIB_DCUF
unknown: F20B10
unknown: F21B10
unknown: F22B10
unknown: F23B10
unknown: F28B10
unknown: F29B10
unknown: F30B10
unknown: F31B10
unknown: F74B10
unknown: F75B10
unknown: F76B10
unknown: F77B10
unknown: F82B10
unknown: F83B10
unknown: F84B10
unknown: F85B10

.tile CIB_R94C52:CIB_DCU3
unknown: F20B10
unknown: F22B10
unknown: F23B10
unknown: F29B10
unknown: F31B10
unknown: F74B10
unknown: F75B10
unknown: F76B10
unknown: F77B10
unknown: F82B10
unknown: F83B10
unknown: F84B10
unknown: F85B10

.tile CIB_R94C53:CIB_DCU2
unknown: F20B10
unknown: F22B10
unknown: F29B10
unknown: F31B10
unknown: F74B10
unknown: F76B10
unknown: F83B10
unknown: F85B10

.tile CIB_R94C54:CIB_DCUG
unknown: F20B10
unknown: F22B10
unknown: F29B10
unknown: F31B10
unknown: F74B10
unknown: F76B10
unknown: F83B10
unknown: F85B10

.tile CIB_R94C55:CIB_DCUH
unknown: F20B10
unknown: F22B10
unknown: F29B10
unknown: F31B10
unknown: F74B10
unknown: F76B10
unknown: F83B10
unknown: F85B10

.tile CIB_R94C56:CIB_DCUI
unknown: F20B10
unknown: F22B10
unknown: F29B10
unknown: F31B10
unknown: F74B10
unknown: F76B10
unknown: F83B10
unknown: F85B10

.tile CIB_R94C57:CIB_DCU1
unknown: F20B10
unknown: F22B10
unknown: F29B10
unknown: F31B10
unknown: F74B10

.tile CIB_R94C6:CIB_EFB0
enum: CIB.JB3MUX 0
enum: CIB.JC6MUX 0
enum: CIB.JD6MUX 0

.tile CIB_R94C71:CIB_DCU0
unknown: F20B10
unknown: F21B10
unknown: F22B10
unknown: F23B10
unknown: F28B10
unknown: F29B10
unknown: F30B10
unknown: F31B10
unknown: F74B10
unknown: F75B10
unknown: F76B10
unknown: F77B10
unknown: F82B10
unknown: F83B10
unknown: F84B10
unknown: F85B10

.tile CIB_R94C72:CIB_DCUA
unknown: F20B10
unknown: F21B10
unknown: F22B10
unknown: F23B10
unknown: F28B10
unknown: F29B10
unknown: F30B10
unknown: F31B10
unknown: F74B10
unknown: F75B10
unknown: F76B10
unknown: F77B10
unknown: F82B10
unknown: F83B10
unknown: F84B10
unknown: F85B10

.tile CIB_R94C73:CIB_DCUB
unknown: F20B10
unknown: F21B10
unknown: F22B10
unknown: F23B10
unknown: F28B10
unknown: F29B10
unknown: F30B10
unknown: F31B10
unknown: F74B10
unknown: F75B10
unknown: F76B10
unknown: F77B10
unknown: F82B10
unknown: F83B10
unknown: F84B10
unknown: F85B10

.tile CIB_R94C74:CIB_DCUC
unknown: F20B10
unknown: F21B10
unknown: F22B10
unknown: F23B10
unknown: F28B10
unknown: F29B10
unknown: F30B10
unknown: F31B10
unknown: F74B10
unknown: F75B10
unknown: F76B10
unknown: F77B10
unknown: F82B10
unknown: F83B10
unknown: F84B10
unknown: F85B10

.tile CIB_R94C75:CIB_DCUD
unknown: F20B10
unknown: F21B10
unknown: F22B10
unknown: F23B10
unknown: F28B10
unknown: F29B10
unknown: F31B10
unknown: F74B10
unknown: F75B10
unknown: F76B10
unknown: F77B10
unknown: F82B10
unknown: F83B10
unknown: F84B10
unknown: F85B10

.tile CIB_R94C76:CIB_DCUF
unknown: F20B10
unknown: F21B10
unknown: F22B10
unknown: F23B10
unknown: F28B10
unknown: F29B10
unknown: F30B10
unknown: F31B10
unknown: F74B10
unknown: F75B10
unknown: F76B10
unknown: F77B10
unknown: F82B10
unknown: F83B10
unknown: F84B10
unknown: F85B10

.tile CIB_R94C77:CIB_DCU3
unknown: F20B10
unknown: F22B10
unknown: F23B10
unknown: F29B10
unknown: F31B10
unknown: F74B10
unknown: F75B10
unknown: F76B10
unknown: F77B10
unknown: F82B10
unknown: F83B10
unknown: F84B10
unknown: F85B10

.tile CIB_R94C78:CIB_DCU2
unknown: F20B10
unknown: F22B10
unknown: F29B10
unknown: F31B10
unknown: F74B10
unknown: F76B10
unknown: F83B10
unknown: F85B10

.tile CIB_R94C79:CIB_DCUG
unknown: F20B10
unknown: F22B10
unknown: F29B10
unknown: F31B10
unknown: F74B10
unknown: F76B10
unknown: F83B10
unknown: F85B10

.tile CIB_R94C7:CIB_EFB1
enum: CIB.JA3MUX 0
enum: CIB.JA4MUX 0
enum: CIB.JA5MUX 0
enum: CIB.JA6MUX 0
enum: CIB.JB3MUX 0
enum: CIB.JB4MUX 0
enum: CIB.JB5MUX 0
enum: CIB.JB6MUX 0
enum: CIB.JC3MUX 0
enum: CIB.JC4MUX 0
enum: CIB.JC5MUX 0
enum: CIB.JD3MUX 0
enum: CIB.JD4MUX 0
enum: CIB.JD5MUX 0

.tile CIB_R94C80:CIB_DCUH
unknown: F20B10
unknown: F22B10
unknown: F29B10
unknown: F31B10
unknown: F74B10
unknown: F76B10
unknown: F83B10
unknown: F85B10

.tile CIB_R94C81:CIB_DCUI
unknown: F20B10
unknown: F22B10
unknown: F29B10
unknown: F31B10
unknown: F74B10
unknown: F76B10
unknown: F83B10
unknown: F85B10

.tile CIB_R94C82:CIB_DCU1
unknown: F20B10
unknown: F22B10
unknown: F29B10
unknown: F31B10
unknown: F74B10

.tile MIB_R10C126:BANKREF2
enum: BANK.VCCIO 3V3

.tile MIB_R12C126:PICR1
enum: PIOD.BASE_TYPE OUTPUT_LVCMOS33
enum: PIOC.BASE_TYPE OUTPUT_LVCMOS33

enum: PIOD.BASE_TYPE OUTPUT_LVCMOS33
enum: PIOC.BASE_TYPE OUTPUT_LVCMOS33

.tile MIB_R14C126:PICR0
enum: PIOA.BASE_TYPE OUTPUT_LVCMOS33
enum: PIOB.BASE_TYPE OUTPUT_LVCMOS33

.tile MIB_R15C126:PICR1_DQS0
enum: PIOC.BASE_TYPE OUTPUT_LVCMOS33
enum: PIOA.BASE_TYPE OUTPUT_LVCMOS33
enum: PIOD.BASE_TYPE OUTPUT_LVCMOS33
enum: PIOB.BASE_TYPE OUTPUT_LVCMOS33

.tile MIB_R16C126:PICR2_DQS1
enum: PIOC.BASE_TYPE OUTPUT_LVCMOS33
enum: PIOD.BASE_TYPE OUTPUT_LVCMOS33

.tile MIB_R18C126:PICR1_DQS3
enum: PIOD.BASE_TYPE INPUT_LVCMOS33
enum: PIOD.HYSTERESIS ON

.tile MIB_R19C126:PICR2
enum: PIOD.BASE_TYPE INPUT_LVCMOS33

.tile MIB_R20C126:PICR0
arc: JDIA JPADDIA_PIO
arc: JDIB JPADDIB_PIO
enum: PIOA.BASE_TYPE INPUT_LVCMOS33
enum: PIOB.BASE_TYPE INPUT_LVCMOS33

.tile MIB_R21C126:PICR1
enum: PIOA.BASE_TYPE INPUT_LVCMOS33
enum: PIOA.HYSTERESIS ON
enum: PIOC.BASE_TYPE INPUT_LVCMOS33
enum: PIOC.HYSTERESIS ON
enum: PIOB.BASE_TYPE INPUT_LVCMOS33
enum: PIOB.HYSTERESIS ON
enum: PIOD.BASE_TYPE INPUT_LVCMOS33
enum: PIOD.HYSTERESIS ON

.tile MIB_R22C126:MIB_CIB_LR_A
enum: PIOC.BASE_TYPE INPUT_LVCMOS33
enum: PIOD.BASE_TYPE INPUT_LVCMOS33

.tile MIB_R22C67:CMUX_UL_0
arc: G_DCS0CLK0 G_VPFN0000

.tile MIB_R22C68:CMUX_UR_0
arc: G_DCS0CLK1 G_VPFN0000

.tile MIB_R29C126:PICR0_DQS2
arc: JDIA JPADDIA_PIO
arc: JDIB JPADDIB_PIO
enum: PIOA.BASE_TYPE INPUT_LVCMOS33
enum: PIOB.BASE_TYPE INPUT_LVCMOS33

.tile MIB_R30C126:PICR1_DQS3
enum: PIOA.BASE_TYPE INPUT_LVCMOS33
enum: PIOA.HYSTERESIS ON
enum: PIOB.BASE_TYPE INPUT_LVCMOS33
enum: PIOB.HYSTERESIS ON

.tile MIB_R35C126:PICR0
arc: JDIA JPADDIA_PIO
arc: JDIB JPADDIB_PIO
enum: PIOB.BASE_TYPE INPUT_LVCMOS33
enum: PIOA.BASE_TYPE INPUT_LVCMOS33

.tile MIB_R36C126:PICR1
enum: PIOD.BASE_TYPE INPUT_LVCMOS33
enum: PIOD.HYSTERESIS ON
enum: PIOC.BASE_TYPE INPUT_LVCMOS33
enum: PIOC.HYSTERESIS ON
enum: PIOB.BASE_TYPE INPUT_LVCMOS33
enum: PIOB.HYSTERESIS ON
enum: PIOA.BASE_TYPE INPUT_LVCMOS33
enum: PIOA.HYSTERESIS ON

.tile MIB_R37C126:PICR2
enum: PIOD.BASE_TYPE INPUT_LVCMOS33
enum: PIOC.BASE_TYPE INPUT_LVCMOS33

.tile MIB_R38C126:PICR0
arc: JDIA JPADDIA_PIO
enum: PIOA.BASE_TYPE INPUT_LVCMOS33

.tile MIB_R39C126:PICR1_DQS0
enum: PIOA.BASE_TYPE INPUT_LVCMOS33
enum: PIOA.HYSTERESIS ON

.tile MIB_R70C67:CMUX_LL_0
arc: G_DCS1CLK0 G_VPFN0000

.tile MIB_R70C68:CMUX_LR_0
arc: G_DCS1CLK1 G_VPFN0000

.tile MIB_R95C101:PICB0
unknown: F0B1

.tile MIB_R95C102:PICB1
unknown: F0B1

.tile MIB_R95C103:PICB0
unknown: F0B1

.tile MIB_R95C104:PICB1
unknown: F0B1

.tile MIB_R95C105:PICB0
unknown: F0B1

.tile MIB_R95C106:PICB1
unknown: F0B1

.tile MIB_R95C107:PICB0
unknown: F0B1

.tile MIB_R95C108:PICB1
unknown: F0B1

.tile MIB_R95C110:PICB0
unknown: F0B1

.tile MIB_R95C111:PICB1
unknown: F0B1

.tile MIB_R95C112:PICB0
unknown: F0B1

.tile MIB_R95C113:PICB1
unknown: F0B1

.tile MIB_R95C114:PICB0
unknown: F0B1

.tile MIB_R95C115:PICB1
unknown: F0B1

.tile MIB_R95C116:PICB0
unknown: F0B1

.tile MIB_R95C117:PICB1
unknown: F0B1

.tile MIB_R95C119:PICB0
unknown: F0B1

.tile MIB_R95C120:PICB1
unknown: F0B1

.tile MIB_R95C121:PICB0
unknown: F0B1

.tile MIB_R95C122:PICB1
unknown: F0B1

.tile MIB_R95C4:EFB0_PICB0
unknown: F54B1
unknown: F56B1
unknown: F82B1
unknown: F94B1

.tile MIB_R95C96:PICB0
unknown: F0B1

.tile MIB_R95C97:PICB1
unknown: F0B1

.tile MIB_R95C98:PICB0
unknown: F0B1

.tile MIB_R95C99:PICB1
unknown: F0B1

.tile R25C124:PLC2
arc: S3_V06S0103 N3_V06S0003

.tile R26C124:PLC2
arc: N3_V06N0103 S3_V06N0003

.tile R29C124:PLC2
arc: S1_V02S0601 E1_H01W0000

.tile R31C124:PLC2
arc: S1_V02S0101 S3_V06N0103
arc: S1_V02S0201 N3_V06S0103
arc: S1_V02S0701 N1_V02S0601

.tile R32C124:PLC2
arc: H00L0000 V02S0201
arc: H00R0100 H02W0501
arc: V00B0000 V02N0201
arc: V00B0100 V02S0101
arc: V00T0100 V02S0701
arc: A0 V02S0701
arc: A1 V02S0701
arc: A2 V02S0701
arc: A3 V02S0701
arc: A4 V00T0100
arc: A5 V00T0100
arc: A6 V00T0100
arc: A7 V00T0100
arc: B0 S1_V02N0301
arc: B1 S1_V02N0301
arc: B2 S1_V02N0301
arc: B3 S1_V02N0301
arc: B4 V02N0501
arc: B5 V02N0501
arc: B6 V02N0501
arc: B7 V02N0501
arc: C0 H02W0601
arc: C1 H02W0601
arc: C2 H02W0601
arc: C3 H02W0601
arc: C4 H02W0601
arc: C5 H02W0601
arc: C6 H02W0601
arc: C7 H02W0601
arc: D0 V02N0201
arc: D1 V02N0201
arc: D2 V02N0201
arc: D3 V02N0201
arc: D4 V00B0000
arc: D5 V00B0000
arc: D6 V00B0000
arc: D7 V00B0000
arc: F0 F5A_SLICE
arc: F1 FXA_SLICE
arc: F2 F5B_SLICE
arc: F3 FXB_SLICE
arc: F4 F5C_SLICE
arc: F5 FXC_SLICE
arc: F6 F5D_SLICE
arc: M0 V00B0100
arc: M1 H00R0100
arc: M2 V00B0100
arc: M3 H00L0000
arc: M4 V00B0100
arc: M5 H00R0100
arc: M6 V00B0100
arc: N3_V06N0003 F3
word: SLICEA.K0.INIT 0000000000000000
word: SLICEA.K1.INIT 1000000000000000
word: SLICEB.K0.INIT 0000000000000000
word: SLICEB.K1.INIT 0000000000000000
word: SLICEC.K0.INIT 0000000000000000
word: SLICEC.K1.INIT 0000000000000000
word: SLICED.K0.INIT 0000000000000000
word: SLICED.K1.INIT 0000000000000000
enum: SLICEA.MODE LOGIC
enum: SLICEA.GSR DISABLED
enum: SLICEA.REG0.SD 0
enum: SLICEA.REG1.SD 0
enum: SLICEA.REG0.REGSET RESET
enum: SLICEA.REG1.REGSET RESET
enum: SLICEA.CEMUX 1
enum: SLICEA.CCU2.INJECT1_0 _NONE_
enum: SLICEA.CCU2.INJECT1_1 _NONE_
enum: SLICEB.MODE LOGIC
enum: SLICEB.GSR DISABLED
enum: SLICEB.REG0.SD 0
enum: SLICEB.REG1.SD 0
enum: SLICEB.REG0.REGSET RESET
enum: SLICEB.REG1.REGSET RESET
enum: SLICEB.CEMUX 1
enum: SLICEB.CCU2.INJECT1_0 _NONE_
enum: SLICEB.CCU2.INJECT1_1 _NONE_
enum: SLICEC.MODE LOGIC
enum: SLICEC.GSR DISABLED
enum: SLICEC.REG0.SD 0
enum: SLICEC.REG1.SD 0
enum: SLICEC.REG0.REGSET RESET
enum: SLICEC.REG1.REGSET RESET
enum: SLICEC.CEMUX 1
enum: SLICEC.CCU2.INJECT1_0 _NONE_
enum: SLICEC.CCU2.INJECT1_1 _NONE_
enum: SLICED.MODE LOGIC
enum: SLICED.GSR DISABLED
enum: SLICED.REG0.SD 0
enum: SLICED.REG1.SD 0
enum: SLICED.REG0.REGSET RESET
enum: SLICED.REG1.REGSET RESET
enum: SLICED.CEMUX 1
enum: SLICED.CCU2.INJECT1_0 _NONE_
enum: SLICED.CCU2.INJECT1_1 _NONE_

.tile R33C124:PLC2
arc: N1_V02N0201 S1_V02N0701
arc: N1_V02N0501 S1_V02N0501

.tile R35C124:PLC2
arc: N1_V02N0501 H02W0501
arc: N1_V02N0701 E1_H01W0100

.tile R37C124:PLC2
arc: N3_V06N0103 E1_H01W0100

"""
