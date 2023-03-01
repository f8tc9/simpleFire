public class SmallEnemy : EnemyController {
    void Start() {
        health = 25;
        fireRate = 0.75f;
    }
}

public class BigEnemy : EnemyController {
    void Start() {
        health = 100;
        fireRate = 1.5f;
    }
}
public class WeaponController : MonoBehaviour {
    public GameObject[] weapons;
    public int currentWeaponIndex = 0;

    void Start() {
        SwitchWeapon(currentWeaponIndex);
    }

    void Update() {
        if (Input.GetKeyDown(KeyCode.Tab)) {
            SwitchWeapon((currentWeaponIndex + 1) % weapons.Length);
        }
    }

    void SwitchWeapon(int weaponIndex) {
        foreach (GameObject weapon in weapons) {
            weapon.SetActive(false);
        }

        weapons[weaponIndex].SetActive(true);
        currentWeaponIndex = weaponIndex;
    }
}

public class AmmoController : MonoBehaviour {
    public int[] ammoCounts;
    public Text[] ammoTexts;

    void Start() {
        UpdateAmmoTexts();
    }

    public void AddAmmo(int weaponIndex, int amount) {
        ammoCounts[weaponIndex] += amount;
        UpdateAmmoTexts();
    }

    public bool UseAmmo(int weaponIndex) {
        if (ammoCounts[weaponIndex] > 0) {
            ammoCounts[weaponIndex]--;
            UpdateAmmoTexts();
            return true;
        }

        return false;
    }

    void UpdateAmmoTexts() {
        for (int i = 0; i < ammoTexts.Length; i++) {
            ammoTexts[i].text = ammoCounts[i].ToString();
        }
    }
}
