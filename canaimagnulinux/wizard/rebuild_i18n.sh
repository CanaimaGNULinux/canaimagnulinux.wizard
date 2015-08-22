rm ./locales/rebuild_i18n.log

DOMAIN='canaimagnulinux.wizard'

i18ndude rebuild-pot --pot ./locales/${DOMAIN}.pot --create ${DOMAIN} ./
i18ndude sync --pot ./locales/${DOMAIN}.pot ./locales/*/LC_MESSAGES/${DOMAIN}.po

#i18ndude rebuild-pot --pot ../i18n/${DOMAIN}-plone.pot --create plone ../profiles ../skins
#i18ndude sync --pot ../i18n/${DOMAIN}-plone.pot ../i18n/${DOMAIN}-plone-*.po

WARNINGS=`find . -name "*pt" | xargs i18ndude find-untranslated | grep -e '^-WARN' | wc -l`
ERRORS=`find . -name "*pt" | xargs i18ndude find-untranslated | grep -e '^-ERROR' | wc -l`
FATAL=`find . -name "*pt"  | xargs i18ndude find-untranslated | grep -e '^-FATAL' | wc -l`

echo
echo "There are $WARNINGS warnings \(possibly missing i18n markup\)"
echo "There are $ERRORS errors \(almost definitely missing i18n markup\)"
echo "There are $FATAL fatal errors \(template could not be parsed, eg. if it\'s not html\)"
echo "For more details, run \'find . -name \"\*pt\" \| xargs i18ndude find-untranslated\' or" 
echo "Look the rebuild i18n log generate for this script called \'rebuild_i18n.log\' on locales dir" 

touch ./locales/rebuild_i18n.log

find ../ -name "*pt" | xargs i18ndude find-untranslated > ./locales/rebuild_i18n.log
