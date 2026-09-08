# K16 prepended-ripple delete--replace no-go

Date: 2026-07-30  
Scope: one deletion from the seven minimum-defect positions of one fixed
authenticated universal word, followed by one arbitrary nonzero one-cell
substitution.

## 1. Frozen word and deletion frontier

Let

\[
T=\texttt{scratch/k16\_12874\_twohole\_partial.word}
\]

have SHA256

```text
a62cb41fc97127edbac362afa0447cf6a45d795f327ec7f2a3652f7c12873181
```

and exact missing masks \(0xa879,0xa87d\).  Put

\[
U=(0xa879)\mathbin\Vert T.
\]

Then \(|U|=12875\), its canonical SHA256 is

```text
74d9aa13a6b9dae664ccbaa744a16efa724acbafee2ed44afc5462a03c5bc441
```

and direct interval-OR replay shows that \(U\) is universal.  The exact
single-deletion census has minimum defect two, attained at precisely the
following seven zero-based positions:

| deleted position in \(U\) | deleted cell | holes after deletion |
|---:|---:|---:|
| 0 | `0xa879` | `0xa879,0xa87d` |
| 1 | `0x882c` | `0xa86d,0xac6d` |
| 2 | `0x2829` | `0x286d,0x2c6d` |
| 6436 | `0x0600` | `0x4e61,0x4e63` |
| 6440 | `0x2879` | `0x2879,0x287d` |
| 12871 | `0x0864` | `0x8ce6,0x9ce6` |
| 12874 | `0xce41` | `0xce61,0xce63` |

In every row the first hole is a proper subset of the second.

## 2. Exact local replacement criterion

Let \(D\) be any word and let \(q\) be a position of \(D\).  Write
\(L_q\) for the multiset of ORs of nonempty suffixes of \(D[0:q]\), and
\(R_q\) for the multiset of ORs of nonempty prefixes of \(D[q+1:|D|]\).
Adjoin the empty mask once to each multiset.  For a proposed replacement
cell \(x\), define

\[
N_q(x)=\{a\vee x\vee b:a\in L_q\cup\{0\},\ b\in R_q\cup\{0\}\}.
\]

Let \(m_D(s)\) be the total interval multiplicity of target \(s\), and let
\(m_{D,q}(s)\) be the multiplicity contributed by intervals containing
position \(q\).  Define the private family

\[
P_q(D)=\{s\ne0:m_D(s)=m_{D,q}(s)>0\}.
\]

Thus \(s\in P_q(D)\) exactly when every old witness for \(s\) contains
\(q\).

**Lemma 2.1 (necessary and sufficient replacement test).**  If \(H(D)\)
is the set of holes of \(D\), replacing \(D_q\) by a nonzero mask \(x\)
gives a universal word if and only if

\[
H(D)\cup P_q(D)\subseteq N_q(x).                 \tag{2.1}
\]

**Proof.** Every interval avoiding \(q\) is unchanged.  Every interval
containing \(q\) is uniquely a suffix to the left of \(q\), the cell at
\(q\), and a prefix to its right; allowing an empty suffix or prefix covers
the endpoint cases.  Consequently the replacement removes exactly the old
local multiplicity \(m_{D,q}\) and installs exactly the labels in \(N_q(x)\).
A previously covered target needs recreation precisely when all its old
witnesses contained \(q\), while every old hole needs a new local witness.
This is exactly (2.1). \(\square\)

**Lemma 2.2 (exact domain reduction for the seven rows).**  Suppose the
holes of \(D\) are \(h\subset h^+\).  If replacing one cell by \(x\) makes
the word universal, then

\[
0<x\subseteq h.                                  \tag{2.2}
\]

**Proof.** Since \(h\) has no old witness, every new witness for \(h\)
contains the replaced cell.  OR is monotone, so every bit of \(x\) belongs
to \(h\).  The word alphabet excludes the zero cell. \(\square\)

Thus arbitrary 16-bit replacement is exhausted by only
\(2^{|h|}-1\), namely 127 or 255, values per position.  This is a proved
domain reduction, not a heuristic candidate restriction.

## 3. Exact result

For each of the seven deletion words, all 12,874 replacement positions and
all nonzero submasks from Lemma 2.2 were checked with Lemma 2.1.  The table
records the number of positions at which some value services both holes,
the total number of hole-serving position/value rows, and the least number
of private targets lost by such a row.

| deletion | domain | service positions | service rows | minimum private debt | rows attaining minimum |
|---:|---:|---:|---:|---:|---:|
| 0 | 255 | 515 | 4192 | 1 | 16 |
| 1 | 255 | 542 | 4133 | 2 | 192 |
| 2 | 127 | 278 | 1439 | 2 | 64 |
| 6436 | 127 | 255 | 801 | 4 | 32 |
| 6440 | 127 | 277 | 1467 | 2 | 72 |
| 12871 | 255 | 462 | 2390 | 3 | 16 |
| 12874 | 255 | 503 | 2157 | 4 | 65 |

In particular no row has private debt zero.

**Theorem 3.1.** There is no universal length-12874 word obtainable from
the authenticated word \(U\) by deleting one of its seven minimum-defect
positions and then replacing one remaining cell by an arbitrary nonzero
16-bit mask.

This rules out exactly the advertised seven-delete/one-replacement
neighborhood.  It does **not** rule out a nonminimum deletion, two or more
substitutions, a general equal-length block replacement, or a genuinely
nonlocal rethreading.

## 4. Replay artifacts

- Exact checker:
  `scratch/audit_r_k16_prepend74d9_delete_replace_20260730.py`
- Concise result and all row digests:
  `scratch/k16_prepend74d9_delete_replace_20260730.audit.json`

The result file distinguishes the SHA of the executed checker from the
current fail-closed checker.  Their only difference is the addition of
hard-coded assertions for the displayed counts and digests; no search logic
changed.
