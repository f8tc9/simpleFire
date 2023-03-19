public class EnemyController : MonoBehaviour {
    public int health = 50;
    public float fireRate = 1f;
    public float movementSpeed = 3f;
    public float detectionRange = 10f;
    public float attackRange = 5f;

    public GameObject bulletPrefab;
    public Transform bulletSpawn;
    public Transform playerTransform;

    private float nextFireTime = 0f;

    void Update() {
        float distanceToPlayer = Vector3.Distance(transform.position, playerTransform.position);

        if (distanceToPlayer <= detectionRange) {
            Vector3 direction = (playerTransform.position - transform.position).normalized;
            transform.LookAt(playerTransform.position);

            if (distanceToPlayer <= attackRange) {
                if (Time.time >= nextFireTime) {
                    nextFireTime = Time.time + fireRate;
                    Shoot();
                }
            } else {
                transform.position += direction * movementSpeed * Time.deltaTime;
            }
        }
    }

    void OnCollisionEnter(Collision collision) {
        if (collision.gameObject.CompareTag("Bullet")) {
            Destroy(collision.gameObject);
            TakeDamage(25);
        }
    }

    void Shoot() {
        GameObject bullet = Instantiate(bulletPrefab, bulletSpawn.position, bulletSpawn.rotation);
        Destroy(bullet, 5f);
    }

    void TakeDamage(int damage) {
        health -= damage;
        if (health <= 0) {
            Destroy(gameObject);
        }
    }
}
public class WeaponManager : MonoBehaviour {
    public static WeaponManager instance;

    public GameObject[] weapons;
    public int currentWeaponIndex = 0;

    void Awake() {
        if (instance == null) {
            instance = this;
            DontDestroyOnLoad(gameObject);
        } else {
            Destroy(gameObject);
        }
    }

    void Start() {
        SetActiveWeapon(currentWeaponIndex);
    }

    void Update() {
        if (Input.GetAxis("Mouse ScrollWheel") > 0f) {
            CycleWeapon(1);
        } else if (Input.GetAxis("Mouse ScrollWheel") < 0f) {
            CycleWeapon(-1);
        }

        if (Input.GetKeyDown(KeyCode.Alpha1)) {
            SetActiveWeapon(0);
        } else if (Input.GetKeyDown(KeyCode.Alpha2)) {
            SetActiveWeapon(1);
        }
    }

    void CycleWeapon(int direction)
