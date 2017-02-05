import React, { Component } from "react";
import { render } from "react-dom";
import { I18nextProvider } from "react-i18next";

import Routes from "Router";
import i18n from "./i18n";

const root = document.querySelector("#root");

render(<I18nextProvider i18n={ i18n }><Routes /></I18nextProvider>, root);
