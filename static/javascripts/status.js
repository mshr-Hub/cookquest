$(function () {

    // ページ読み込み時にランダムでstatusを決定
    let hp = Math.ceil( Math.random()*1000 );
    let mp = Math.ceil( Math.random()*1000 );
    let atk = Math.ceil( Math.random()*1000 );
    let def = Math.ceil( Math.random()*1000 );

    $('.hp').html(`<small class="quest-font"><i class="fas fa-heart"></i> HP: </small>
                    ${hp}`);

    $('.mp').html(`<small class="quest-font"><i class="fas fa-hat-wizard"></i> MP: </small>
                    ${mp}`);

    $('.atk').html(`<small class="quest-font"><i class="fas fa-bomb"></i> ATK: </small>
                    ${atk}`);

    $('.def').html(`<small class="quest-font"><i class="fas fa-shield-alt"></i> DEF: </small>
                    ${def}`);

});
