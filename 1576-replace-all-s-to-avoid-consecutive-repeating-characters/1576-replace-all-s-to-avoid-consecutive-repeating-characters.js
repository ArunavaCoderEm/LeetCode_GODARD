/**
 * @param {string} 
 * @return {string}
 */

function allCharactersSame(s){
    let n = s.length;
    for (let i = 1; i < n; i++)
        if (s[i] != s[0])
            return false;

    return true;
}
var modifyString = function(s) {
    const t = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];
    if(allCharactersSame(s)){
        s = s.replaceAll("??",'ac');
    }
    for (var i = 0; i < s.length; ++i){
        if(s[i] === '?'){
            s = s.replace(s[i],t.find(y => y !== s[i - 1] && y !== s[i + 1]),);
        }
    }    
    return s;
};