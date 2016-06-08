// ‎靠北工程師74102‬ 
// https://www.facebook.com/kobeengineer/photos/a.1634720690097535.1073741828.1632027893700148/1778232339079702/?type=3&theater

function factorial(num)
{
  if (num === 0)
    { return 1; }
  else
    { return num * factorial( num - 1 ); }
}

function fact_str(asm)
{
  var asm_return_value = factorial(asm).toString();
  return asm_return_value;
}

function zero_clac(zcs)
{
  var zcs_input = fact_str(zcs);
  var count = 0;
  for ( var i=0; i<zcs_input.length; i++ )
  {
    if ( zcs_input[i] == "0" ) { count++; }
  }
  return count;
}

console.log( zero_clac(100) );