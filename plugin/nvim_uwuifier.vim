if !has('python3')
    echomsg ':python3 is not available, nvim uwuifier will not be loaded.'
    finish
endif

python3 import nvim_uwuifier.uwuifier
python3 uwuifier = nvim_uwuifier.uwuifier.Uwuifier(vim)
function! UwuifyRange(start, end)
  python3 start = int(vim.eval('a:start')) - 1
  python3 end = int(vim.eval('a:end'))
  python3 uwuifier.uwuify_range(start, end)
endfunction

command! -range=% UwU call UwuifyRange(<line1>, <line2>)

