import { Module } from "module";

class ModuleScript {
	static evaluateAttribute(content) {
		const AsyncFunction = (async function () {}).constructor;
		return new AsyncFunction(`return ${content};`);
	}

	static getModule(content, filePath) {
		let m = new Module();
		// m.paths = module.paths;

		}
		m._compile(content, filePath);
		return m.exports;
	}
}

export { ModuleScript };