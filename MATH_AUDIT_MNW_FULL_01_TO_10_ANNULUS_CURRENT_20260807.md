# Audit: full `01 -> 10` B8 annulus current

Base B8 q2 current:

```text
+11101101 +11010111 -11100111 -10111110.
```

Destination minus source gives the shell:

```text
+1011101101 +1011010111 +0111100111 +0110111110
-1011100111 -1010111110 -0111101101 -0111010111.
```

Adding the natural `01` source packet cancels its four terms and leaves

```text
+1011101101 +1011010111 -1011100111 -1010111110.
```

Suffix restriction separates every different Dyck up-set, so no two
suffix currents cancel.  At general width q, an ordered chronology
conjugacy gives destination current minus source current; it is zero iff
the base q-current is zero.  Under the same ordered socket bijection,
source and destination reconnection permutations are conjugate, so the
shell is component-neutral and the carried B8 packet retains component
change `-5` per suffix.

**Verdict:** incidence telescoping PASS; explicit q2 formula PASS under
turn faithfulness; topology/all-width reduction PASS under chronology and
socket faithfulness; literal host planting and finite base q3+ audit OPEN.
