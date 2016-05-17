/**
 * Created by Administrator on 2015/12/9.
 */
(function(window, document, undefined){
  var $ROOT = $("#NTGUID__2");
  var $TPLS = NodeTpl._tpls["http://s.lietou-static.com/revs/tpls/www/beta2/user/landingpage_form_b2479eb6.js"];
  var $DATA = NodeTpl._data["NDTGUID__2"];
var form = $("form", $ROOT);
LT.File.Js.load("http://core.pc.lietou-static.com/revs/js/common/plugins/jquery.checkboxui_1589ca87.js,http://core.pc.lietou-static.com/revs/js/common/plugins/jquery.placeholderui_4ea8db00.js", function () {
  $(".checkbox", $ROOT).CheckboxUI();
  $('[placeholder]', $ROOT).PlaceholderUI();
});
$(".goLogin", $ROOT).bind("click", function () {
  LT.User.requireLogin({
    register: false
  }, function () {
    window.location.href = LT.Env.wwwRoot + "home/?r=" + Math.random();
  });
});
var changeCode = $('.changecode', $ROOT),
  validCode = changeCode.siblings('.validcode', $ROOT),
  cRegister = $('.register-box', $ROOT);
LT.File.Js.load("http://s.lietou-static.com/revs/p/beta2/js/plugins/jquery.validTip_3908ed67.js,http://core.pc.lietou-static.com/revs/js/common/plugins/jquery.valid_cbce39ff.js", function () {
  changeCode.add(validCode).bind("click", function () {
    $(this).closest('form').find('.image-verycode').attr("src", "/image/randomcode/?" + Math.random());
    //validCode.attr("src","/image/randomcode/?"+ Math.random());
    return false;
  });
  // 手机号注册新加
  var phoneCodeWrap = $('[data-selector="phone-code-wrap"]', cRegister),
    emailCodeWrap = $('[data-selector="email-code-wrap"]', cRegister),
    phoneCodeBtn = $('[data-selector="phone-code-btn"]', phoneCodeWrap).data('times', 0),
    checkEmail = $('[data-selector="checkEmail"]', cRegister);
  // 倒计时
  function countdown(elm, time) {
      if (!elm) {
        return false;
      }
      var elm = elm,
        start = time || 60,
        timer = null;
      elm.removeClass('btn-primary').addClass('btn-disabled');
      (function () {
        start--;
        elm.html('重新获取（' + start + '）');
        if (start <= 0) {
          elm.removeClass('btn-disabled').addClass('btn-primary').html('重新获取');
          clearTimeout(timer);
          return false;
        }
        timer = setTimeout(arguments.callee, 1000);
      })();
    }
    // 获取手机验证码
  phoneCodeBtn.bind('click', function () {
    if ($(this).hasClass('btn-disabled')) {
      return false;
    }
    if (!checkEmail.attr('data-valid') || checkEmail.attr('data-valid') == 'false') {
      checkEmail.trigger("highlight", true).trigger('focus');
      return false;
    }
    var $this = $(this),
      times = $this.data('times') - 0;
    if (LT.Cookie.get('phone_code_times') == 1) {
      countdown($this);
      return false;
    }
    if (times >= 3) {
      $this.data('times', 0);
      LT.Cookie.set('phone_code_times', 1, 1 / 24 / 2);
      countdown($this);
      checkEmail.SimpleValidErrorTips('如果您一直无法收到验证码，请用邮箱注册');
      return false;
    }
    $.ajax({
      url: LT.Env.wwwRoot + 'user/sendverifymessage?__mn__=newtel',
      type: 'POST',
      data: 'newtel=' + $.trim(checkEmail.val()),
      dataType: 'json',
      success: function (data) {
        if (data.flag == 1) {
          times++;
          $this.data('times', times);
          countdown($this);
        } else {
          $.dialog.error(data.msg);
        }
      },
      error: function (data) {
        $.dialog.error(data.msg);
      }
    });
  });
  cRegister.valid({
    scan: function (data) {
      if (!data.valid) {
        $.each(data.result, function (i, n) {
          !n.valid && n.element.trigger("highlight", true);
        });
        data.firstError.element.triggerHandler("focus");
      } else {
        cRegister.find(".text-error").removeClass("text-error");
      }
    },
    dynrule: {
      "checkPhoneEmail": function () {
        if (LT.String.isEmail($(this).val())) {
          emailCodeWrap.show().find('input').prop('disabled', false);
          phoneCodeWrap.hide().find('input').prop('disabled', true);
          return [
            ['email', '请输入正确的$'],
            ['ajax', 'checkMailExist', '该邮箱已注册，请更换邮箱']
          ]; //邮箱
        } else if (LT.String.isMobile($(this).val())) {
          emailCodeWrap.hide().find('input').prop('disabled', true);
          phoneCodeWrap.show().find('input').prop('disabled', false);
          return [
            ['phone', '请输入正确的$']
          ]; //手机号
        } else {
          return [
            ['phone', '请输入正确的$'],
            ['email', '请输入正确的$']
          ];
        }
      }
    },
    ajax: {
      "checkMailExist": {
        url: LT.Env.wwwRoot + "user/isuserexist/",
        data: function () {
          return {
            user_login: $('[data-selector="checkEmail"]', cRegister).val()
          };
        },
        dataType: "json",
        cache: false,
        success: function (data) {
          if (data == 1) {
            $('[data-selector="checkEmail"]', cRegister).trigger("highlight", true);
            return false; // 验证未通过
          } else {
            return true; // 验证通过
          }
        }
      }
    },
    success: function () {
      var $this = $(this);
      var _pw = $('[name="web_user.user_pwd"]', cRegister),
        _pw_val = _pw.val();
      if (/\b(000000|111111|11111111|112233|123123|123321|123456|12345678|654321|666666|888888|1234567)\b/.test(_pw_val)) {
        _pw.SimpleValidErrorTips('密码安全度低，请更换密码');
        return false;
      }
      if (/"|'|<|>|\?|\%|\*/g.test(_pw_val)) {
        _pw.SimpleValidErrorTips('请使用常用符号');
        return false;
      }
      $.ajax({
        url: $this.attr("action"),
        type: $this.attr("method"),
        data: $this.serializeArray(),
        dataType: "json",
        cache: false,
        success: function (data) {
          if (data.success) {
            var srId = '';
            if (cRegister.attr('sr_id')) {
              srId = '?sr_id=' + cRegister.attr('sr_id');
            }
            $DATA.callback && $DATA.callback();
            window.location.href = "/user/regc/regnamecard/" + srId;
          } else {
            $(".changecode", $this).trigger("click");
            if (data.msg.indexOf("验证码") >= 0) {
              $('input[name="rand"]', $this).filter(function () {
                if (!this.disabled) {
                  return this;
                }
              }).SimpleValidErrorTips(data.msg);
            } else {
              $('[data-selector="checkEmail"]', $this).SimpleValidErrorTips(data.msg);
            }
          }
        },
        mask: $(':submit', $this)
      });
      return false;
    }
  });
  $("[validate-rules]").SimpleValidTips();
});
})(window, document);
delete NodeTpl._data["NDTGUID__2"];

