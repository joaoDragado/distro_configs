"use strict";
// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License.
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __param = (this && this.__param) || function (paramIndex, decorator) {
    return function (target, key) { decorator(target, key, paramIndex); }
};
Object.defineProperty(exports, "__esModule", { value: true });
const inversify_1 = require("inversify");
require("reflect-metadata");
const types_1 = require("../../../ioc/types");
const types_2 = require("../../../linters/types");
const constants_1 = require("../../constants");
const types_3 = require("../../types");
const main_1 = require("./main");
let ErrorHandlerFactory = class ErrorHandlerFactory {
    constructor(installer, logger, outputChannel, linterHelper, serviceContainer) {
        this.installer = installer;
        this.logger = logger;
        this.outputChannel = outputChannel;
        this.linterHelper = linterHelper;
        this.serviceContainer = serviceContainer;
    }
    create(product) {
        return new main_1.ErrorHandler(product, this.installer, this.linterHelper, this.logger, this.outputChannel, this.serviceContainer);
    }
};
ErrorHandlerFactory = __decorate([
    inversify_1.injectable(),
    __param(0, inversify_1.inject(types_3.IInstaller)),
    __param(1, inversify_1.inject(types_3.ILogger)),
    __param(2, inversify_1.inject(types_3.IOutputChannel)), __param(2, inversify_1.named(constants_1.STANDARD_OUTPUT_CHANNEL)),
    __param(3, inversify_1.inject(types_2.ILinterHelper)),
    __param(4, inversify_1.inject(types_1.IServiceContainer))
], ErrorHandlerFactory);
exports.ErrorHandlerFactory = ErrorHandlerFactory;
//# sourceMappingURL=factory.js.map