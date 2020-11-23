import styles from './File.module.css';

export const File = () => {
  return (
    <div className={styles.wrapper}>
      <div className={styles.container}>
        <div className={styles.title}>The Knights Who Say Ni</div>
        <div className={styles.knightPhoto}>Knight Photo</div>
      </div>

      <div className={styles.container}>
        <div className={styles.title}>Living as a Newt</div>
        <div className={styles.cureInstructions}>
          Wait until you get better.
        </div>
      </div>

      <div className={styles.treeContainer}>
        <div className={styles.title}>How to Cut Down a Mighty Tree?</div>
        <div className={styles.herringPhoto}>Herring Photo</div>
        <div className={styles.coconutHorsePhoto}>Horse Photo</div>
      </div>
    </div>
  );
};
