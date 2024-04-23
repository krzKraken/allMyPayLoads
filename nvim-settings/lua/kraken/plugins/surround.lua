return {
  "kylechui/nvim-surround",
  event = { "BufReadPre", "BufNewFile" },
  version = "*", -- Use for stability; omit to use `main` branch for the latest features
  config = true,
}

-- Para palabra simple ysiw + " o ' 
-- Eliminar ds + "
-- Cambiar de " a ' -> cs + " + '
-- Agregar tag ys + (2j dos lineas o $ fin de linea ) + t (ponemos nombre de tag)
-- Cambiar tag cs + t (el nuevo tag) 
