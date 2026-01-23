/** @type {import('tailwindcss').Config} */
module.exports = {
  "theme": {
    "extend": {
      "colors": {
        "transparent": "#000000",
        "white": "#ffffff",
        "black": "#000000",
        "alpha": {
          "white": "#0c0e12",
          "black": "#ffffff"
        },
        "brand": {
          "25": "#fcfaff",
          "50": "#f9f5ff",
          "100": "#f4ebff",
          "200": "#e9d7fe",
          "300": "#d6bbfb",
          "400": "#b692f6",
          "500": "#9e77ed",
          "600": "#7f56d9",
          "700": "#6941c6",
          "800": "#53389e",
          "900": "#42307d",
          "950": "#2c1c5f"
        },
        "error": {
          "25": "#fffbfa",
          "50": "#fef3f2",
          "100": "#fee4e2",
          "200": "#fecdca",
          "300": "#fda29b",
          "400": "#f97066",
          "500": "#f04438",
          "600": "#d92d20",
          "700": "#b42318",
          "800": "#912018",
          "900": "#7a271a",
          "950": "#55160c"
        },
        "warning": {
          "25": "#fffcf5",
          "50": "#fffaeb",
          "100": "#fef0c7",
          "200": "#fedf89",
          "300": "#fec84b",
          "400": "#fdb022",
          "500": "#f79009",
          "600": "#dc6803",
          "700": "#b54708",
          "800": "#93370d",
          "900": "#7a2e0e",
          "950": "#4e1d09"
        },
        "success": {
          "25": "#f6fef9",
          "50": "#ecfdf3",
          "100": "#dcfae6",
          "200": "#abefc6",
          "300": "#75e0a7",
          "400": "#47cd89",
          "500": "#17b26a",
          "600": "#079455",
          "700": "#067647",
          "800": "#085d3a",
          "900": "#074d31",
          "950": "#053321"
        },
        "gray": {
          "25": "#fafafa",
          "50": "#f7f7f7",
          "100": "#f0f0f1",
          "200": "#ececed",
          "300": "#cecfd2",
          "400": "#94979c",
          "500": "#85888e",
          "600": "#61656c",
          "700": "#373a41",
          "800": "#22262f",
          "900": "#13161b",
          "950": "#0c0e12",
          "blue": {
            "25": "#fcfcfd",
            "50": "#f8f9fc",
            "100": "#eaecf5",
            "200": "#d5d9eb",
            "300": "#b3b8db",
            "400": "#717bbc",
            "500": "#4e5ba6",
            "600": "#3e4784",
            "700": "#363f72",
            "800": "#293056",
            "900": "#101323",
            "950": "#0d0f1c"
          },
          "cool": {
            "25": "#fcfcfd",
            "50": "#f9f9fb",
            "100": "#eff1f5",
            "200": "#dcdfea",
            "300": "#b9c0d4",
            "400": "#7d89b0",
            "500": "#5d6b98",
            "600": "#4a5578",
            "700": "#404968",
            "800": "#30374f",
            "900": "#111322",
            "950": "#0e101b"
          },
          "modern": {
            "25": "#fcfcfd",
            "50": "#f8fafc",
            "100": "#eef2f6",
            "200": "#e3e8ef",
            "300": "#cdd5df",
            "400": "#9aa4b2",
            "500": "#697586",
            "600": "#4b5565",
            "700": "#364152",
            "800": "#202939",
            "900": "#121926",
            "950": "#0d121c"
          },
          "neutral": {
            "25": "#fcfcfd",
            "50": "#f9fafb",
            "100": "#f3f4f6",
            "200": "#e5e7eb",
            "300": "#d2d6db",
            "400": "#9da4ae",
            "500": "#6c737f",
            "600": "#4d5761",
            "700": "#384250",
            "800": "#1f2a37",
            "900": "#111927",
            "950": "#0d121c"
          },
          "iron": {
            "25": "#fcfcfc",
            "50": "#fafafa",
            "100": "#f4f4f5",
            "200": "#e4e4e7",
            "300": "#d1d1d6",
            "400": "#a0a0ab",
            "500": "#70707b",
            "600": "#51525c",
            "700": "#3f3f46",
            "800": "#26272b",
            "900": "#1a1a1e",
            "950": "#131316"
          },
          "true": {
            "25": "#fcfcfc",
            "50": "#f7f7f7",
            "100": "#f5f5f5",
            "200": "#e5e5e5",
            "300": "#d6d6d6",
            "400": "#a3a3a3",
            "500": "#737373",
            "600": "#525252",
            "700": "#424242",
            "800": "#292929",
            "900": "#141414",
            "950": "#0f0f0f"
          },
          "warm": {
            "25": "#fdfdfc",
            "50": "#fafaf9",
            "100": "#f5f5f4",
            "200": "#e7e5e4",
            "300": "#d7d3d0",
            "400": "#a9a29d",
            "500": "#79716b",
            "600": "#57534e",
            "700": "#44403c",
            "800": "#292524",
            "900": "#1c1917",
            "950": "#171412"
          }
        },
        "moss": {
          "25": "#fafdf7",
          "50": "#f5fbee",
          "100": "#e6f4d7",
          "200": "#ceeab0",
          "300": "#acdc79",
          "400": "#86cb3c",
          "500": "#669f2a",
          "600": "#4f7a21",
          "700": "#3f621a",
          "800": "#335015",
          "900": "#2b4212",
          "950": "#1a280b"
        },
        "green": {
          "25": "#f6fef9",
          "50": "#edfcf2",
          "100": "#d3f8df",
          "200": "#aaf0c4",
          "300": "#73e2a3",
          "400": "#3ccb7f",
          "500": "#16b364",
          "600": "#099250",
          "700": "#087443",
          "800": "#095c37",
          "900": "#084c2e",
          "950": "#052e1c",
          "light": {
            "25": "#fafef5",
            "50": "#f3fee7",
            "100": "#e3fbcc",
            "200": "#d0f8ab",
            "300": "#a6ef67",
            "400": "#85e13a",
            "500": "#66c61c",
            "600": "#4ca30d",
            "700": "#3b7c0f",
            "800": "#326212",
            "900": "#2b5314",
            "950": "#15290a"
          }
        },
        "teal": {
          "25": "#f6fefc",
          "50": "#f0fdf9",
          "100": "#ccfbef",
          "200": "#99f6e0",
          "300": "#5fe9d0",
          "400": "#2ed3b7",
          "500": "#15b79e",
          "600": "#0e9384",
          "700": "#107569",
          "800": "#125d56",
          "900": "#134e48",
          "950": "#0a2926"
        },
        "cyan": {
          "25": "#f5feff",
          "50": "#ecfdff",
          "100": "#cff9fe",
          "200": "#a5f0fc",
          "300": "#67e3f9",
          "400": "#22ccee",
          "500": "#06aed4",
          "600": "#088ab2",
          "700": "#0e7090",
          "800": "#155b75",
          "900": "#164c63",
          "950": "#0d2d3a"
        },
        "blue": {
          "25": "#f5faff",
          "50": "#eff8ff",
          "100": "#d1e9ff",
          "200": "#b2ddff",
          "300": "#84caff",
          "400": "#53b1fd",
          "500": "#2e90fa",
          "600": "#1570ef",
          "700": "#175cd3",
          "800": "#1849a9",
          "900": "#194185",
          "950": "#102a56",
          "light": {
            "25": "#f5fbff",
            "50": "#f0f9ff",
            "100": "#e0f2fe",
            "200": "#b9e6fe",
            "300": "#7cd4fd",
            "400": "#36bffa",
            "500": "#0ba5ec",
            "600": "#0086c9",
            "700": "#026aa2",
            "800": "#065986",
            "900": "#0b4a6f",
            "950": "#062c41"
          },
          "dark": {
            "25": "#f5f8ff",
            "50": "#eff4ff",
            "100": "#d1e0ff",
            "200": "#b2ccff",
            "300": "#84adff",
            "400": "#528bff",
            "500": "#2970ff",
            "600": "#155eef",
            "700": "#004eeb",
            "800": "#0040c1",
            "900": "#00359e",
            "950": "#002266"
          }
        },
        "indigo": {
          "25": "#f5f8ff",
          "50": "#eef4ff",
          "100": "#e0eaff",
          "200": "#c7d7fe",
          "300": "#a4bcfd",
          "400": "#8098f9",
          "500": "#6172f3",
          "600": "#444ce7",
          "700": "#3538cd",
          "800": "#2d31a6",
          "900": "#2d3282",
          "950": "#1f235b"
        },
        "violet": {
          "25": "#fbfaff",
          "50": "#f5f3ff",
          "100": "#ece9fe",
          "200": "#ddd6fe",
          "300": "#c3b5fd",
          "400": "#a48afb",
          "500": "#875bf7",
          "600": "#7839ee",
          "700": "#6927da",
          "800": "#5720b7",
          "900": "#491c96",
          "950": "#2e125e"
        },
        "purple": {
          "25": "#fafaff",
          "50": "#f4f3ff",
          "100": "#ebe9fe",
          "200": "#d9d6fe",
          "300": "#bdb4fe",
          "400": "#9b8afb",
          "500": "#7a5af8",
          "600": "#6938ef",
          "700": "#5925dc",
          "800": "#4a1fb8",
          "900": "#3e1c96",
          "950": "#27115f"
        },
        "fuchsia": {
          "25": "#fefaff",
          "50": "#fdf4ff",
          "100": "#fbe8ff",
          "200": "#f6d0fe",
          "300": "#eeaafd",
          "400": "#e478fa",
          "500": "#d444f1",
          "600": "#ba24d5",
          "700": "#9f1ab1",
          "800": "#821890",
          "900": "#6f1877",
          "950": "#47104c"
        },
        "pink": {
          "25": "#fef6fb",
          "50": "#fdf2fa",
          "100": "#fce7f6",
          "200": "#fcceee",
          "300": "#faa7e0",
          "400": "#f670c7",
          "500": "#ee46bc",
          "600": "#dd2590",
          "700": "#c11574",
          "800": "#9e165f",
          "900": "#851651",
          "950": "#4e0d30"
        },
        "rose": {
          "25": "#fff5f6",
          "50": "#fff1f3",
          "100": "#ffe4e8",
          "200": "#fecdd6",
          "300": "#fea3b4",
          "400": "#fd6f8e",
          "500": "#f63d68",
          "600": "#e31b54",
          "700": "#c01048",
          "800": "#a11043",
          "900": "#89123e",
          "950": "#510b24"
        },
        "orange": {
          "25": "#fefaf5",
          "50": "#fef6ee",
          "100": "#fdead7",
          "200": "#f9dbaf",
          "300": "#f7b27a",
          "400": "#f38744",
          "500": "#ef6820",
          "600": "#e04f16",
          "700": "#b93815",
          "800": "#932f19",
          "900": "#772917",
          "950": "#511c10",
          "dark": {
            "25": "#fff9f5",
            "50": "#fff4ed",
            "100": "#ffe6d5",
            "200": "#ffd6ae",
            "300": "#ff9c66",
            "400": "#ff692e",
            "500": "#ff4405",
            "600": "#e62e05",
            "700": "#bc1b06",
            "800": "#97180c",
            "900": "#771a0d",
            "950": "#57130a"
          }
        },
        "yellow": {
          "25": "#fefdf0",
          "50": "#fefbe8",
          "100": "#fef7c3",
          "200": "#feee95",
          "300": "#fde272",
          "400": "#fac515",
          "500": "#eaaa08",
          "600": "#ca8504",
          "700": "#a15c07",
          "800": "#854a0e",
          "900": "#713b12",
          "950": "#542c0d"
        },
        "utility": {
          "blue": {
            "50": "var(--color-blue-950)",
            "100": "var(--color-blue-900)",
            "200": "var(--color-blue-800)",
            "300": "var(--color-blue-700)",
            "400": "var(--color-blue-600)",
            "500": "var(--color-blue-500)",
            "600": "var(--color-blue-400)",
            "700": "var(--color-blue-300)",
            "dark": {
              "50": "var(--color-blue-dark-950)",
              "100": "var(--color-blue-dark-900)",
              "200": "var(--color-blue-dark-800)",
              "300": "var(--color-blue-dark-700)",
              "400": "var(--color-blue-dark-600)",
              "500": "var(--color-blue-dark-500)",
              "600": "var(--color-blue-dark-400)",
              "700": "var(--color-blue-dark-300)"
            },
            "light": {
              "50": "var(--color-blue-light-950)",
              "100": "var(--color-blue-light-900)",
              "200": "var(--color-blue-light-800)",
              "300": "var(--color-blue-light-700)",
              "400": "var(--color-blue-light-600)",
              "500": "var(--color-blue-light-500)",
              "600": "var(--color-blue-light-400)",
              "700": "var(--color-blue-light-300)"
            }
          },
          "brand": {
            "50": "var(--color-brand-950)",
            "100": "var(--color-brand-900)",
            "200": "var(--color-brand-800)",
            "300": "var(--color-brand-700)",
            "400": "var(--color-brand-600)",
            "500": "var(--color-brand-500)",
            "600": "var(--color-brand-400)",
            "700": "var(--color-brand-300)",
            "800": "var(--color-brand-200)",
            "900": "var(--color-brand-100)",
            "50_alt": "var(--color-utility-gray-50)",
            "100_alt": "var(--color-utility-gray-100)",
            "200_alt": "var(--color-utility-gray-200)",
            "300_alt": "var(--color-utility-gray-300)",
            "400_alt": "var(--color-utility-gray-400)",
            "500_alt": "var(--color-utility-gray-500)",
            "600_alt": "var(--color-utility-gray-600)",
            "700_alt": "var(--color-utility-gray-700)",
            "800_alt": "var(--color-utility-gray-800)",
            "900_alt": "var(--color-utility-gray-900)"
          },
          "gray": {
            "50": "var(--color-gray-900)",
            "100": "var(--color-gray-800)",
            "200": "var(--color-gray-700)",
            "300": "var(--color-gray-700)",
            "400": "var(--color-gray-600)",
            "500": "var(--color-gray-500)",
            "600": "var(--color-gray-400)",
            "700": "var(--color-gray-300)",
            "800": "var(--color-gray-200)",
            "900": "var(--color-gray-100)",
            "blue": {
              "50": "var(--color-gray-blue-950)",
              "100": "var(--color-gray-blue-900)",
              "200": "var(--color-gray-blue-800)",
              "300": "var(--color-gray-blue-700)",
              "400": "var(--color-gray-blue-600)",
              "500": "var(--color-gray-blue-500)",
              "600": "var(--color-gray-blue-400)",
              "700": "var(--color-gray-blue-300)"
            }
          },
          "error": {
            "50": "var(--color-error-950)",
            "100": "var(--color-error-900)",
            "200": "var(--color-error-800)",
            "300": "var(--color-error-700)",
            "400": "var(--color-error-600)",
            "500": "var(--color-error-500)",
            "600": "var(--color-error-400)",
            "700": "var(--color-error-300)"
          },
          "warning": {
            "50": "var(--color-warning-950)",
            "100": "var(--color-warning-900)",
            "200": "var(--color-warning-800)",
            "300": "var(--color-warning-700)",
            "400": "var(--color-warning-600)",
            "500": "var(--color-warning-500)",
            "600": "var(--color-warning-400)",
            "700": "var(--color-warning-300)"
          },
          "success": {
            "50": "var(--color-success-950)",
            "100": "var(--color-success-900)",
            "200": "var(--color-success-800)",
            "300": "var(--color-success-700)",
            "400": "var(--color-success-600)",
            "500": "var(--color-success-500)",
            "600": "var(--color-success-400)",
            "700": "var(--color-success-300)"
          },
          "orange": {
            "50": "var(--color-orange-950)",
            "100": "var(--color-orange-900)",
            "200": "var(--color-orange-800)",
            "300": "var(--color-orange-700)",
            "400": "var(--color-orange-600)",
            "500": "var(--color-orange-500)",
            "600": "var(--color-orange-400)",
            "700": "var(--color-orange-300)",
            "dark": {
              "50": "var(--color-orange-dark-950)",
              "100": "var(--color-orange-dark-900)",
              "200": "var(--color-orange-dark-800)",
              "300": "var(--color-orange-dark-700)",
              "400": "var(--color-orange-dark-600)",
              "500": "var(--color-orange-dark-500)",
              "600": "var(--color-orange-dark-400)",
              "700": "var(--color-orange-dark-300)"
            }
          },
          "indigo": {
            "50": "var(--color-indigo-950)",
            "100": "var(--color-indigo-900)",
            "200": "var(--color-indigo-800)",
            "300": "var(--color-indigo-700)",
            "400": "var(--color-indigo-600)",
            "500": "var(--color-indigo-500)",
            "600": "var(--color-indigo-400)",
            "700": "var(--color-indigo-300)"
          },
          "fuchsia": {
            "50": "var(--color-fuchsia-950)",
            "100": "var(--color-fuchsia-900)",
            "200": "var(--color-fuchsia-800)",
            "300": "var(--color-fuchsia-700)",
            "400": "var(--color-fuchsia-600)",
            "500": "var(--color-fuchsia-500)",
            "600": "var(--color-fuchsia-400)",
            "700": "var(--color-fuchsia-300)"
          },
          "pink": {
            "50": "var(--color-pink-950)",
            "100": "var(--color-pink-900)",
            "200": "var(--color-pink-800)",
            "300": "var(--color-pink-700)",
            "400": "var(--color-pink-600)",
            "500": "var(--color-pink-500)",
            "600": "var(--color-pink-400)",
            "700": "var(--color-pink-300)"
          },
          "purple": {
            "50": "var(--color-purple-950)",
            "100": "var(--color-purple-900)",
            "200": "var(--color-purple-800)",
            "300": "var(--color-purple-700)",
            "400": "var(--color-purple-600)",
            "500": "var(--color-purple-500)",
            "600": "var(--color-purple-400)",
            "700": "var(--color-purple-300)"
          },
          "green": {
            "50": "var(--color-green-950)",
            "100": "var(--color-green-900)",
            "200": "var(--color-green-800)",
            "300": "var(--color-green-700)",
            "400": "var(--color-green-600)",
            "500": "var(--color-green-500)",
            "600": "var(--color-green-400)",
            "700": "var(--color-green-300)"
          },
          "yellow": {
            "50": "var(--color-yellow-950)",
            "100": "var(--color-yellow-900)",
            "200": "var(--color-yellow-800)",
            "300": "var(--color-yellow-700)",
            "400": "var(--color-yellow-600)",
            "500": "var(--color-yellow-500)",
            "600": "var(--color-yellow-400)",
            "700": "var(--color-yellow-300)"
          }
        },
        "text": {
          "white": "var(--color-white)",
          "primary": "var(--color-gray-50)",
          "secondary": "var(--color-gray-300)",
          "secondary_hover": "var(--color-gray-200)",
          "tertiary": "var(--color-gray-400)",
          "tertiary_hover": "var(--color-gray-300)",
          "quaternary": "var(--color-gray-400)",
          "error": {
            "primary": "var(--color-error-400)",
            "primary_hover": "var(--color-error-300)"
          },
          "warning": {
            "primary": "var(--color-warning-400)"
          },
          "success": {
            "primary": "var(--color-success-400)"
          },
          "disabled": "var(--color-gray-500)",
          "placeholder": "var(--color-gray-500)",
          "placeholder_subtle": "var(--color-gray-700)",
          "editor": {
            "icon": {
              "fg": "var(--color-gray-400)",
              "fg_active": "var(--color-white)"
            }
          },
          "primary_on": {
            "brand": "var(--color-gray-50)"
          },
          "secondary_on": {
            "brand": "var(--color-gray-300)"
          },
          "tertiary_on": {
            "brand": "var(--color-gray-400)"
          },
          "quaternary_on": {
            "brand": "var(--color-gray-400)"
          },
          "brand": {
            "primary": "var(--color-gray-50)",
            "secondary": "var(--color-gray-300)",
            "secondary_hover": "var(--color-gray-200)",
            "tertiary": "var(--color-gray-400)",
            "tertiary_alt": "var(--color-gray-50)"
          }
        },
        "border": {
          "primary": "var(--color-gray-700)",
          "secondary": "var(--color-gray-800)",
          "secondary_alt": "var(--color-gray-800)",
          "tertiary": "var(--color-gray-800)",
          "error": "var(--color-error-400)",
          "error_subtle": "var(--color-error-500)",
          "disabled": "var(--color-gray-700)",
          "disabled_subtle": "var(--color-gray-800)",
          "brand": "var(--color-brand-400)",
          "brand_alt": "var(--color-gray-700)"
        },
        "fg": {
          "white": "var(--color-white)",
          "primary": "var(--color-white)",
          "secondary": "var(--color-gray-300)",
          "secondary_hover": "var(--color-gray-200)",
          "tertiary": "var(--color-gray-400)",
          "tertiary_hover": "var(--color-gray-300)",
          "quaternary": "var(--color-gray-600)",
          "quaternary_hover": "var(--color-gray-500)",
          "warning": {
            "primary": "var(--color-warning-500)",
            "secondary": "var(--color-warning-400)"
          },
          "success": {
            "primary": "var(--color-success-500)",
            "secondary": "var(--color-success-400)"
          },
          "error": {
            "primary": "var(--color-error-500)",
            "secondary": "var(--color-error-400)"
          },
          "disabled": "var(--color-gray-500)",
          "disabled_subtle": "var(--color-gray-600)",
          "brand": {
            "primary": "var(--color-brand-500)",
            "primary_alt": "var(--color-gray-300)",
            "secondary": "var(--color-brand-500)",
            "secondary_alt": "var(--color-gray-600)",
            "secondary_hover": "var(--color-gray-500)"
          }
        },
        "bg": {
          "primary": "var(--color-gray-950)",
          "primary_alt": "var(--color-bg-secondary)",
          "primary_hover": "var(--color-gray-800)",
          "secondary": "var(--color-gray-900)",
          "secondary_subtle": "var(--color-gray-900)",
          "secondary_hover": "var(--color-gray-800)",
          "secondary_alt": "var(--color-bg-primary)",
          "tertiary": "var(--color-gray-800)",
          "quaternary": "var(--color-gray-700)",
          "error": {
            "primary": "var(--color-error-950)",
            "secondary": "var(--color-error-600)",
            "solid": "var(--color-error-600)",
            "solid_hover": "var(--color-error-500)"
          },
          "warning": {
            "primary": "var(--color-warning-950)",
            "secondary": "var(--color-warning-600)",
            "solid": "var(--color-warning-600)"
          },
          "success": {
            "primary": "var(--color-success-950)",
            "secondary": "var(--color-success-600)",
            "solid": "var(--color-success-600)"
          },
          "disabled": "var(--color-gray-800)",
          "disabled_subtle": "var(--color-gray-900)",
          "active": "var(--color-gray-800)",
          "overlay": "var(--color-gray-800)",
          "brand": {
            "primary": "var(--color-brand-500)",
            "primary_alt": "var(--color-bg-secondary)",
            "secondary": "var(--color-brand-600)",
            "solid": "var(--color-brand-600)",
            "solid_hover": "var(--color-brand-500)",
            "section": "var(--color-bg-secondary)",
            "section_subtle": "var(--color-bg-primary)"
          }
        },
        "app": {
          "store": {
            "badge": {
              "border": "var(--color-white)"
            }
          }
        },
        "avatar": {
          "bg": "var(--color-gray-800)",
          "contrast": {
            "border": "#ffffff"
          },
          "profile": {
            "photo": {
              "border": "var(--color-gray-950)"
            }
          },
          "styles": {
            "bg": {
              "neutral": "#e0e0e0"
            }
          }
        },
        "button": {
          "destructive": {
            "primary": {
              "icon": "var(--color-error-300)",
              "icon_hover": "var(--color-error-200)"
            }
          },
          "primary": {
            "icon": "var(--color-brand-300)",
            "icon_hover": "var(--color-brand-200)"
          }
        },
        "featured": {
          "icon": {
            "light": {
              "fg": {
                "brand": "var(--color-brand-200)",
                "error": "var(--color-error-200)",
                "gray": "var(--color-gray-200)",
                "success": "var(--color-success-200)",
                "warning": "var(--color-warning-200)"
              }
            }
          }
        },
        "focus": {
          "ring": "var(--color-brand-500)"
        },
        "footer": {
          "button": {
            "fg": "var(--color-gray-300)",
            "fg_hover": "var(--color-gray-100)"
          }
        },
        "icon": {
          "fg": {
            "brand": "var(--color-gray-400)",
            "brand_on": {
              "brand": "var(--color-gray-400)"
            }
          }
        },
        "screen": {
          "mockup": {
            "border": "var(--color-gray-700)"
          }
        },
        "slider": {
          "handle": {
            "bg": "var(--color-fg-brand-primary)",
            "border": "var(--color-bg-primary)"
          }
        },
        "toggle": {
          "border": "var(--color-transparent)",
          "button": {
            "fg_disabled": "var(--color-gray-600)"
          },
          "slim": {
            "border_pressed": "var(--color-transparent)"
          }
        },
        "tooltip": {
          "supporting": {
            "text": "var(--color-gray-300)"
          }
        },
        "nav": {
          "item": {
            "button": {
              "icon": {
                "fg": "var(--color-gray-400)",
                "fg_active": "var(--color-gray-300)"
              }
            },
            "icon": {
              "fg": "var(--color-gray-400)",
              "fg_active": "var(--color-gray-300)"
            }
          }
        }
      },
      "fontFamily": {
        "body": "var(--font-inter, \"Inter\"), -apple-system, \"Segoe UI\", Roboto, Arial, sans-serif",
        "display": "var(--font-inter, \"Inter\"), -apple-system, \"Segoe UI\", Roboto, Arial, sans-serif",
        "mono": "ui-monospace, \"Roboto Mono\", SFMono-Regular, Menlo, Monaco, Consolas, \"Liberation Mono\", \"Courier New\", monospace"
      },
      "fontSize": {
        "xs": "calc(var(--spacing) * 3)",
        "sm": "calc(var(--spacing) * 3.5)",
        "md": "calc(var(--spacing) * 4)",
        "lg": "calc(var(--spacing) * 4.5)",
        "xl": "calc(var(--spacing) * 5)",
        "display-xs": "calc(var(--spacing) * 6)",
        "display-sm": "calc(var(--spacing) * 7.5)",
        "display-md": "calc(var(--spacing) * 9)",
        "display-lg": "calc(var(--spacing) * 12)",
        "display-xl": "calc(var(--spacing) * 15)",
        "display-2xl": "calc(var(--spacing) * 18)"
      },
      "lineHeight": {
        "xsline": "calc(var(--spacing) * 4.5)",
        "smline": "calc(var(--spacing) * 5)",
        "mdline": "calc(var(--spacing) * 6)",
        "lgline": "calc(var(--spacing) * 7)",
        "xlline": "calc(var(--spacing) * 7.5)",
        "display-xsline": "calc(var(--spacing) * 8)",
        "display-smline": "calc(var(--spacing) * 9.5)",
        "display-mdline": "calc(var(--spacing) * 11)",
        "display-lgline": "calc(var(--spacing) * 15)",
        "display-xlline": "calc(var(--spacing) * 18)",
        "display-2xlline": "calc(var(--spacing) * 22.5)"
      },
      "letterSpacing": {
        "display-mdletter": "-0.72px",
        "display-lgletter": "-0.96px",
        "display-xlletter": "-1.2px",
        "display-2xlletter": "-1.44px"
      },
      "borderRadius": {
        "none": "0px",
        "xs": "0.125rem",
        "sm": "0.25rem",
        "DEFAULT": "0.25rem",
        "md": "0.375rem",
        "lg": "0.5rem",
        "xl": "0.75rem",
        "2xl": "1rem",
        "3xl": "1.5rem",
        "full": "9999px"
      },
      "boxShadow": {
        "xs": "0px 1px 2px rgba(10, 13, 18, 0.05)",
        "sm": "0px 1px 3px rgba(10, 13, 18, 0.1), 0px 1px 2px -1px rgba(10, 13, 18, 0.1)",
        "md": "0px 4px 6px -1px rgba(10, 13, 18, 0.1), 0px 2px 4px -2px rgba(10, 13, 18, 0.06)",
        "lg": "0px 12px 16px -4px rgba(10, 13, 18, 0.08), 0px 4px 6px -2px rgba(10, 13, 18, 0.03), 0px 2px 2px -1px rgba(10, 13, 18, 0.04)",
        "xl": "0px 20px 24px -4px rgba(10, 13, 18, 0.08), 0px 8px 8px -4px rgba(10, 13, 18, 0.03), 0px 3px 3px -1.5px rgba(10, 13, 18, 0.04)",
        "2xl": "0px 24px 48px -12px rgba(10, 13, 18, 0.18), 0px 4px 4px -2px rgba(10, 13, 18, 0.04)",
        "3xl": "0px 32px 64px -12px rgba(10, 13, 18, 0.14), 0px 5px 5px -2.5px rgba(10, 13, 18, 0.04)",
        "skeumorphic": "0px 0px 0px 1px rgba(10, 13, 18, 0.18) inset, 0px -2px 0px 0px rgba(10, 13, 18, 0.05) inset",
        "modern-mockup-inner-lg": "0px 0px 3.765px 1.255px rgba(10, 13, 18, 0.08) inset, 0px 0px 2.51px 1.255px rgba(10, 13, 18, 0.03) inset",
        "modern-mockup-inner-md": "0px 0px 1.692px 0.564px rgba(10, 13, 18, 0.08) inset, 0px 0px 1.128px 0.564px rgba(10, 13, 18, 0.03) inset",
        "modern-mockup-inner-sm": "0px 0px 4.48px 1.493px rgba(10, 13, 18, 0.08) inset, 0px 0px 2.987px 1.493px rgba(10, 13, 18, 0.03) inset",
        "modern-mockup-outer-lg": "0px 7.529px 10.039px -2.51px rgba(10, 13, 18, 0.08), 0px 2.51px 3.765px -1.255px rgba(10, 13, 18, 0.03),\n        0px 1.255px 1.255px -0.627px rgba(10, 13, 18, 0.04)",
        "modern-mockup-outer-md": "0px 3.385px 4.513px -1.128px rgba(10, 13, 18, 0.08), 0px 1.128px 1.692px -0.564px rgba(10, 13, 18, 0.03),\n        0px 0.564px 0.564px -0.282px rgba(10, 13, 18, 0.04)"
      },
      "animation": {
        "marquee": "marquee 60s linear infinite",
        "caret-blink": "caret-blink 1s infinite"
      },
      "screens": {
        "xxs": "320px",
        "xs": "600px"
      },
      "spacing": {
        "max-container": "1280px"
      }
    }
  }
};