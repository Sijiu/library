/**
 * Created by Administrator on 2015/12/9.
 */
var Register = {
    code: 0,
    number: 0,
    email_num: 0,
    init: function () {
        Register.mobile = $("#r-mobile");
        Register.mobile.bind("blur", Register.verify);
    },
    verify: function () {
        var mobile = Register.mobile.val();
        if (/^1[3|4|5|7|8|9][0-9]\d{4,8}$/.test(mobile)) {
            Register.write_error("shuruZhengque");
        }
    },
    write_error: function write_error(error){
        var msg = $(".error-msg");
        msg.text(error);
    }
}
$(function(){
    Register.init();
})