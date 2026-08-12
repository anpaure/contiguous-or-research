# Independent full-cell audit of the (j=3959) outer Hall collars

Date: 2026-07-30  
Lane: AD independent audit  
Status: **PASS at the stated finite local scope**

## 1. Audited objects

The canonical files were read but not modified:

- `scratch/build_k16_j3959_outer_hall_collar_catalogue_20260730.py`;
- `scratch/k16_j3959_outer_hall_collar_20260730/local_collars.tsv`;
- `scratch/k16_j3959_outer_hall_collar_20260730/local_collars.audit.json`.

The independent checker and its outputs are:

- `scratch/audit_k16_j3959_outer_hall_collar_full_cells_20260730.py`;
- `scratch/k16_j3959_outer_hall_collar_full_cells_audit_20260730/independent_full_cells.audit.json`;
- `scratch/k16_j3959_outer_hall_collar_full_cells_audit_20260730/failed_role_cells.tsv`.

The source builder's `candidate()` routine checks only the saved mandatory
mask and the union envelope.  In particular, it does not explicitly check
(E_p\cap T\ne\varnothing) at every position of the proposed cell.  The
purpose of this audit was to decide whether that source-level omission makes
any of the 57,396 saved rows false.

## 2. Exact local cell criterion

Let (R_0,\ldots,R_{18}) be one saved collar and put

\[
 E_p=R_{p-2}\cap R_{p-1}\cap R_p\qquad(2\le p\le18).
\]

For every completely contextualized row (2\le r\le16) and bit (b\in R_r),
its local carrier is

\[
 C_{r,b}=\{p\in\{r,r+1,r+2\}:b\in E_p\}.
\]

For an advertised interval (I=[a,b)), define

\[
 U(I)=\bigcup_{p\in I}E_p,
 \qquad
 M(I)=\{x:\text{some }C_{r,x}\subseteq I\}.
\]

### Lemma 2.1 (exact one-cell criterion)

Keeping the maximal letters (A_p=E_p) outside (I), there are nonempty
letters (A_p\subseteq E_p) inside (I) which preserve every row
(R_2,\ldots,R_{16}) and satisfy

\[
 \bigcup_{p\in I}A_p=T
\]

if and only if

\[
 M(I)\subseteq T\subseteq U(I)
 \quad\text{and}\quad
 E_p\cap T\ne\varnothing\quad\text{for every }p\in I.
\]

#### Proof

Necessity of (T\subseteq U(I)) and the nonempty-intersection conditions is
immediate from nonempty (A_p\subseteq E_p) and their union being (T).  If
some (x\in M(I)\setminus T), one contextualized row has every carrier of
(x) inside (I); all its letters omit (x), so that row is not preserved.

Conversely take (A_p=E_p\cap T) inside (I) and (A_p=E_p) outside.
Every inside letter is nonempty by hypothesis, and their union is (T)
because (T\subseteq U(I)).  A row bit can disappear only if all of its
carriers lie in (I) and the bit is absent from (T), which is excluded by
(M(I)\subseteq T).  Hence all contextualized rows replay exactly. 

## 3. Finite audit theorem

### Theorem 3.1

For every one of the 57,396 saved collars, the three advertised intervals for

\[
 Q=\mathtt{8000},\qquad P=\mathtt{2665},\qquad S=\mathtt{0665}
\]

are distinct and satisfy the full criterion of Lemma 2.1.  Consequently all
57,396 saved collars really have the three claimed exact local Hall cells.

The exact counts are:

- 57,396 of 57,396 collars pass;
- all 2,250 service blocks retain at least one collar;
- each of the three right ports retains exactly 19,132 collars;
- the (Q)-cell is always `[7,8)`;
- the (P)-cell is always `[14,16)`;
- the (S)-cell is `[15,16)` in 57,216 collars and `[2,4)` in 180 collars.

There are zero failures of (M(I)\subseteq T), (T\subseteq U(I)), or any
per-position (E_p\cap T\ne\varnothing) condition.  On these particular
advertised cells, the fully recomputed carrier mandatory mask never exceeds
the producer's singleton-carrier mandatory mask.  Thus the producer routine
is not generic as written, but both omitted tests happen to be redundant on
the emitted catalogue.

#### Independent replay details

For every TSV row the checker additionally:

1. re-read all 19 collar values from the 19 saved, pairwise distinct physical
   indices in the authoritative (j=3959) word;
2. checked the six service-block rows against the authoritative block file;
3. checked the consecutive predecessor packet, fixed left port, selected
   right port, two extra right-context rows, the listed level-one completion,
   and the level-two boundary test;
4. rebuilt every (E_p) from the row values without importing the producer;
5. verified
   (R_r=E_r\cup E_{r+1}\cup E_{r+2}) for every (2\le r\le16);
6. rebuilt the complete carrier-derived (M(I)) and explicitly installed the
   canonical letters from Lemma 2.1.

All six checks pass for all 57,396 rows.

### Theorem 3.2 (strong simultaneous local witness)

For every saved collar, one local letter vector realizes all three advertised
role intervals simultaneously while preserving all contextualized rows.

#### Proof by exact finite replay

Starting from (A_p=E_p), the checker intersects (A_p) with every role
target whose interval contains (p).  It then verifies nonemptiness of every
letter, the three exact interval OR identities, and all fifteen contextualized
row identities.  The failure count is zero in each right-port class.  This is
stronger than merely finding three distinct vertices in the candidate graph.

## 4. Exact scope boundary

This audit proves a finite **local** statement only.  It does not prove that a
collar can be embedded into the full chronology while preserving source
occurrences, flats, arbitrary-depth upper traces, or global Hall zero.  Those
are exactly the remaining source-compensated global-embedding obligations.

The only negative source finding is code-scope hygiene: `candidate()` is not a
sound generic exact-cell predicate because it omits the per-position
nonempty-intersection test, and the producer's mandatory construction need
not account for a multi-position carrier captured by a longer interval.  No
saved advertised role cell exercises either defect.

