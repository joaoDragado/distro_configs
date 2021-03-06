"use strict";
// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License.
Object.defineProperty(exports, "__esModule", { value: true });
// tslint:disable-next-line:no-import-side-effect
require("reflect-metadata");
const decoder_1 = require("./decoder");
const proc_1 = require("./proc");
const pythonExecutionFactory_1 = require("./pythonExecutionFactory");
const types_1 = require("./types");
function registerTypes(serviceManager) {
    serviceManager.addSingleton(types_1.IBufferDecoder, decoder_1.BufferDecoder);
    serviceManager.addSingleton(types_1.IProcessService, proc_1.ProcessService);
    serviceManager.addSingleton(types_1.IPythonExecutionFactory, pythonExecutionFactory_1.PythonExecutionFactory);
}
exports.registerTypes = registerTypes;
//# sourceMappingURL=serviceRegistry.js.map