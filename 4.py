public class LevelManager : MonoBehaviour {
    public static LevelManager instance;

    public GameObject[] levels;
    public int currentLevelIndex = 0;

    void Awake() {
        if (instance == null) {
            instance = this;
            DontDestroyOnLoad(gameObject);
        } else {
            Destroy(gameObject);
        }
    }

    void Start() {
        LoadLevel(currentLevelIndex);
    }

    public void LoadNextLevel() {
        currentLevelIndex++;
        LoadLevel(currentLevelIndex);
    }

    void LoadLevel(int levelIndex) {
        foreach (GameObject level in levels) {
            level.SetActive(false);
        }

        levels[levelIndex].SetActive(true);
    }
}
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class PlayerController : MonoBehaviour {
    public float moveSpeed = 5f;
    public float jumpForce = 5f;

    public GameObject bulletPrefab;
    public Transform bulletSpawn;

    private Rigidbody rb;
    private bool isGrounded = true;

    void Start() {
        rb = GetComponent<Rigidbody>();
    }

    void Update() {
        float hAxis = Input.GetAxis("Horizontal");
        float vAxis = Input.GetAxis("Vertical");

        Vector3 movement = new Vector3(hAxis, 0, vAxis) * moveSpeed * Time.deltaTime;
        transform.Translate(movement, Space.Self);

        if (Input.GetButtonDown("Jump") && isGrounded) {
            rb.AddForce(Vector3.up * jumpForce, ForceMode.Impulse);
            isGrounded = false;
        }

        if (Input.GetButtonDown("Fire1")) {
            Shoot();
        }
    }

    void OnCollisionEnter(Collision collision) {
        if (collision.gameObject.CompareTag("Ground")) {
            isGrounded = true;
        }
    }

    void Shoot() {
        GameObject bullet = Instantiate(bulletPrefab, bulletSpawn.position, bulletSpawn.rotation);
        Destroy(bullet, 5f);
    }
}

public class EnemyController : MonoBehaviour {
    public int health = 50;
    public float fireRate = 1f;

    private float nextFireTime = 0f;

    void Update() {
        if (Time.time >= nextFireTime) {
            nextFireTime = Time.time + fireRate;
            Shoot();
        }
    }

    void OnCollisionEnter(Collision collision) {
        if (collision.gameObject.CompareTag("Bullet")) {
            Destroy(collision.gameObject);
            TakeDamage(25);
        }
    }

    void Shoot() {
        // TODO: Implement enemy shooting logic
    }

    void TakeDamage(int damage) {
        health -= damage;
        if (health <= 0) {
            Destroy(gameObject);
        }
    }
