# Audit: closed two-hex endpoint packet

**Date:** 2026-08-07  
**Method:** independent incidence and q2 replay; no computation or search

The companion hex has vertex row

```text
1100100101 1100110101 1100110100
1101110100 1101100100 1101100101
```

and alternating status word `101010`.  Its endpoint owners are
`1100110100` and `1101100100`; only `1100100101` contributes a turn:

```text
1100111101 -> 1101101101.
```

The deleted target has witnesses `(5,8)` and `(6,7)`, so one remains.

The leaf face current is

```text
+1010101111 -0110101111,
```

and the deleted target has witnesses `(5,9)` and `(3,10)`.  Supports of the
two faces are disjoint.  Their total current is therefore

```text
+1010101111 +1101101101 -0110101111 -1100111101,
```

with both negative targets retaining one provider.

**Verdict:** PASS for literal q1 degree preservation, exact q2 support, and
Dyck suffix tensoring.  Annulus and component claims remain open.

