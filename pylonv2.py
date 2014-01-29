#!/usr/bin/python3.3
#Command line will have script and fields
#Todo: execute scripts in parallel
import inspect
import pdb
import argparse
import re
pdb.set_trace()

def getAllArgs():
        parser = argparse.ArgumentParser()
        parser.add_argument("script")
        parser.add_argument('fields', metavar='Arguments', type=str, nargs='+', help='Input your fileds in the same order as you defined them')
        return parser.parse_args()

def dumpInputs(databin, inputArgs, internalInputArgs):
        for idx, var in enumerate(internalInputArgs):
                databin[var] = inputArgs[idx]
        return databin

def dumpVars(databin, internalVars):
        for k, v in internalVars.items():
                 databin[k] = v
        return databin

def getFunctions(script):
        return inspect.getmembers(script, inspect.isfunction)

def updateVarTable(databin):
        varTable = {}
        for key, val in databin.items():
                if databin[key] is '':
                       updateVarTable.varTable[key] = False
                else:
                       updateVarTable.varTable[key] = True
updateVarTable.varTable = {}

def updateFuncTable(databin):
        for function in updateFuncTable.funcTable.keys():
                functioninputs = inspect.getargspec(function[1]).args
                varcount = len(functioninputs)
                vartruecount = 0

                for var in functioninputs:
                        if updateVarTable.varTable[var] is True:
                                vartruecount += 1

                if varcount == vartruecount:
                        updateFuncTable.funcTable[function] = True
updateFuncTable.funcTable = {}

def initFuncRanTable(functions):
        for function in functions:
                initFuncRanTable.funcRanTable[function]= False
initFuncRanTable.funcRanTable = {}

def getDatabin():
        return getDatabin.databin
getDatabin.databin = {}

def setupVars(script, allArgs):
        databin = {}
        databin = dumpInputs(databin, allArgs.fields, typeToArray(script.arguments))
        databin = dumpVars(databin, cleanDict(script.internalData.__dict__))
        return databin

def typeToArray(rawType):
        return [item for item in dir(rawType) if not item.startswith("__")]

def cleanDict(rawDict):
        return {k: v for k, v in rawDict.items() if not k.startswith("__")}

def setupFuncs(script):
        all_functions = getFunctions(script)
        initFuncRanTable(all_functions)
        for function in all_functions:
                updateFuncTable.funcTable[function] = False
        return all_functions

def dataflowAlgorithm(functions, databin, script):
        completed = False
        while not completed:
                updateVarTable(databin)
                updateFuncTable(databin)
                for function in functions:
                        if updateFuncTable.funcTable[function] & initFuncRanTable.funcRanTable[function] is False:
                                databin = execute(function, databin, script)
                                initFuncRanTable.funcRanTable[function] = True
                completed = areWeThereYet()

def areWeThereYet():
        areWeThereYet.loopCounter += 1
        funcCount = len(updateFuncTable.funcTable)

        if all(updateFuncTable.funcTable.values()) is True:
                return True
        if areWeThereYet.loopCounter == funcCount:
                return True
        else:
                return False
areWeThereYet.loopCounter = 0

def execute(function, databin, script):
        argstring = []
        functioninputs = inspect.getargspec(function[1]).args

        for var in functioninputs:
                argstring.append(databin[var])
        functionReturn = getattr(script, function[0])(*argstring)

        if functionReturn != None:
                for key in functionReturn.keys():
                        databin[key] = functionReturn[key]

        return databin

def main():
        allArgs = getAllArgs()
        script = __import__(allArgs.script)
        databin = setupVars(script, allArgs)
        getDatabin.databin = databin
        functions = setupFuncs(script)
        dataflowAlgorithm(functions, databin, script)

if  __name__ =='__main__':
        main()
