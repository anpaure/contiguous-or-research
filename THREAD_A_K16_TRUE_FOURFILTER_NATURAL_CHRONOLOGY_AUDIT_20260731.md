# Genuine four-filter K16 natural chronology: reconstruction and exact compiler audit

Date: 2026-07-31  
Lane: A  
Status: proved for the authenticated natural target order; not a K16 lower bound

## 1. Lineage and reconstruction

The genuine four-filter parent is

```text
scratch/K15_FOURFILTER_SEED_20260731.word
SHA-256 51f57125ea3e145e08ed9d5f8816d22313a010907588457260c824c6f40217f4
```

with frozen metadata

```text
opening = (5134,0,5,1,0), direction = forward,
(deficit,repetitions,singletons,t62) = (0,0,0,26).
```

None of the historically misnamed `e483...`, `def4`, `cut1004`, or
endpoint-transport artifacts enters the theorem below: those belong to the
separately audited seed0-derived basin.

Let \(w=(w_0,\ldots,w_{6437})\), and define

\[
D_3(i)=w_i\vee w_{i+1}\vee w_{i+2}\vee w_{i+3},\qquad
D_2(i)=w_i\vee w_{i+1}\vee w_{i+2}.
\]

The 6,435 values \(D_3(i)\) are the complete rank-eight layer of
\([15]\), without repetition. The 6,436 values \(D_2(i)\) consist of the
complete rank-seven layer, without repetition, and the unique rank-six
exception

\[
D_2(6390)=\mathtt{0x13c8}.
\]

Put \(z=2^{15}=\mathtt{0x8000}\) and define

\[
T=operatorname{rev}\bigl(z\vee D_2[0,6390)\bigr)
  \;\Vert\;D_3
  \;\Vert\;\operatorname{rev}\bigl(z\vee D_2[6391,6436)\bigr). \tag{1.1}
\]

The decimal, space-separated, newline-terminated form of (1.1) is

```text
scratch/k16_true_fourfilter_natural_targets_20260731.word
SHA-256 0f6d64e9311ef634169964350baa8f817b17b9d1619970c881f87e7346550a5c
```

Its three \(z\)-phase runs have lengths \(6390,6435,45\) and phases
\((1,0,1)\).

## 2. Exact carrier language

Write \(N=\binom{15}{8}=6435\), \(B_i=D_2(i)\) for
\(0\leq i\leq N\), and \(A_i=D_3(i)\) for \(0\leq i<N\).

### Lemma 2.1 (one-defect lift)

Suppose that the \(A_i\) enumerate all rank-eight subsets of \([15]\),
that a unique \(B_s\) has rank six, and that the remaining \(B_i\)
enumerate all rank-seven subsets of \([15]\). Then

\[
T_s=(z\vee B_{s-1},\ldots,z\vee B_0,
     A_0,\ldots,A_{N-1},
     z\vee B_N,\ldots,z\vee B_{s+1}) \tag{2.1}
\]

enumerates the complete middle layer of \([16]\). Every consecutive pair
in (2.1) is a Johnson edge except possibly \(A_{s-1},A_s\). Consequently,
\(T_s\) is a linear Hamilton path if and only if
\(\lvert A_{s-1}\cap A_s\rvert=7\).

Moreover, the tagged adjacent unions inside the two lifted wings are
\(z\vee A_j\) for every \(j\notin\{s-1,s\}\); the two phase seams merely
duplicate \(z\vee A_0\) and \(z\vee A_{N-1}\). Hence the tagged q1 palette
has the two forced holes \(z\vee A_{s-1}\) and \(z\vee A_s\).

#### Proof

The middle layer of \([16]\) partitions into old rank-eight sets and
\(z\) joined to old rank-seven sets. The hypotheses and omission of
\(B_s\) therefore prove exact ownership. The identities

\[
B_i\vee B_{i-1}=A_{i-1},\qquad
B_0\subset A_0,qquad B_N\subset A_{N-1}
\]

give all lifted-wing and phase-seam Johnson edges. Also
\(B_i\subset A_{i-1}\cap A_i\) for every interior \(i\); this gives a
rank-seven intersection unless \(i=s\), where \(B_s\) has rank six. This
proves the sole exceptional-edge criterion. Taking unions in the same
identities gives the tagged q1 assertion. ∎

For the authenticated parent, \(s=6390\),

\[
B_s=\mathtt{0x13c8},\quad
A_{s-1}=\mathtt{0x53cc},\quad
A_s=\mathtt{0x33cc},\quad
A_{s-1}\cap A_s=\mathtt{0x13cc},
\]

so the exceptional intersection has rank seven.

### Theorem 2.2

The sequence \(T\) is a linear Hamilton path of \(J(16,8)\). It is not a
cycle: its endpoints are `0xd38c` and `0xb1cc`, whose symmetric difference
has size four. Its adjacent-union rank-nine language misses exactly

\[
\{\mathtt{0xb3cc},\mathtt{0xd3cc}\}. \tag{2.2}
\]

The multiplicities of its 11,438 represented q1 colours are

\[
1^{10107},\qquad 2^{1231},\qquad 3^{100}. \tag{2.3}
\]

Its complete arbitrary-width upper deficit is

\[
\{\mathtt{0xb3cc},\mathtt{0xd3cc},
  \mathtt{0xd3ce},\mathtt{0xdbce},
  \mathtt{0xf3cc},\mathtt{0xfbce}\}. \tag{2.4}
\]

The rank distribution in (2.4) is \((2,2,1,1)\) at ranks
\((9,10,11,12)\), and zero thereafter.

#### Proof

The two rank-seven pieces of \(D_2\) in (1.1), together with the \(D_3\)
piece, give all \(\binom{16}{8}=12870\) rank-eight masks exactly once.
Direct adjacent replay gives symmetric difference two at all 12,869
internal adjacencies, including the two phase junctions. Thus \(T\) is a
linear Johnson Hamilton path. Lemma 2.1 gives the two tagged holes in
(2.2); exhaustive adjacent replay also shows that every untagged rank-nine
colour is present and gives (2.3).

For the all-upper assertion, propagate at each position the distinct ORs of
all intervals ending there. Comparing this exhaustive recurrence with every
mask of ranks 9 through 16 gives exactly (2.4). This is not a bounded-window
test. ∎

The six holes in (2.4) have an exact gap-crossing description. If

\[
H[a,b]=z\vee\bigvee_{i=a}^{b}B_i,
\]

then they are

\[
\begin{aligned}
H[s,s+1]&=\mathtt{0xb3cc},& H[s-1,s]&=\mathtt{0xd3cc},\\
H[s-2,s]&=\mathtt{0xd3ce},& H[s-1,s+1]&=\mathtt{0xf3cc},\\
H[s-3,s]&=\mathtt{0xdbce},& H[s-3,s+1]&=\mathtt{0xfbce}.
\end{aligned} \tag{2.5}
\]

Indeed, every lifted-\(B\) interval avoiding \(s\) survives in one of the
two wings, while an interval crossing the omitted \(B_s\) needs an
alternative witness. Exhaustive interval replay proves that precisely the
six local words in (2.5) lack one. Thus the upper defect is a transport
tower created by the split at \(B_s\), not an unstructured census. The
exactness of this six-word list is instance-specific; it is not forced by
the hypotheses of Lemma 2.1 alone.

## 3. Exact all-schedule scalar obstruction

A three-hole monotone P/Q schedule deletes three starts \(X\) and three
deadlines \(Y\), pairs the remaining starts and deadlines in order, and has
row spans at most three. Its selected proper-prefix area is

\[
A(X,Y)=\sum_i(q_i-p_i).
\]

### Theorem 3.1

Over every realizable three-hole monotone P/Q schedule inducing the fixed
order \(T\),

\[
\max A(X,Y)=25744. \tag{3.1}
\]

The lexicographically first maximizer is

\[
X=\{12826,12827,12872\},\qquad
Y=\{0,6390,6391\}. \tag{3.2}
\]

Its span histogram is \(1^{6433}3^{6437}\). Even granting every omitted
start the uniform maximum of three lower cells gives

\[
25744+9=25753<26332=\sum_{r=1}^{7}\binom{16}{r}. \tag{3.3}
\]

At the actual endpoint positions in (3.2), the omitted-start credit is only
\(3+3+1=7\), so the exact physical lower-cell count is 25,751. Consequently
no three-hole monotone P/Q compiler with this fixed target order can cover
every nonempty lower target.

#### Proof

After each physical position, retain the event-DAG state

\[
\bigl(|X\cap[0,p]|,|Y\cap[0,p]|,
  \text{the ordered OR accumulators of all active middle rows}\bigr).
\]

For a fixed state, all future legal actions and all future area increments
are identical, so retaining the largest accumulated area is exact. The
terminal state with three start holes, three deadline holes, and no active
row yields (3.1) and (3.2). Every maximizing envelope is nonzero and
literally replays its middle row. Equation (3.3) is a necessary scalar
capacity condition and fails by 579. ∎

## 4. Generalized Hall at the maximizing schedule

Although Theorem 3.1 already kills the entire fixed-order fibre, the
maximizing schedule was also audited against every individually feasible
lower-prefix pin.

### Theorem 4.1

For schedule (3.2), the exact generalized lower incidence graph has 25,751
cells and 343,156 incidences. Its maximum matching is

\[
22822/26332, \tag{4.1}
\]

so its deficiency is 3,510. Its canonical alternating Hall shore has 9,949
targets and 6,439 neighbouring cells. Its twelve zero-host targets are

```text
8000 8001 8002 8004 8010 8020
8040 8200 8400 8800 a000 c000
```

#### Proof

For each physical lower cell \(J\), let \(E_p\) be the maximal envelope at
position \(p\), let \(O_J=\bigvee_{p\in J}E_p\), and let \(M_J\) be the
bits whose complete active-row host interval is contained in \(J\). A lower
target \(S\) is individually feasible at \(J\) exactly when

\[
M_J\subseteq S\subseteq O_J,
\qquad E_p\cap S\ne\varnothing\quad(p\in J).
\]

Enumerating precisely these incidences and applying Hopcroft--Karp gives
(4.1). Alternating reachability from all exposed targets gives the stated
9,949/6,439 shore, whose difference is 3,510. ∎

The frozen Hall audit is

```text
scratch/k16_true_fourfilter_natural_maxarea_generalized_hall_20260731.audit.json
SHA-256 a43a4555f3996b5a1a07ee5cdcc851f9667a847dac138be2773195c7a8f223ab
payload 5911b3400d62842fe175198d9884480ddea604bec1d48abc4c755c29fe20d153
```

## 5. Exact boundary

The authenticated natural chronology is closed in the three-hole monotone
P/Q architecture. This is stronger than failure of one displayed Hall
graph: (3.1) is the global scalar maximum over every schedule in that
fixed-order class.

The result does **not** exclude:

1. rethreading the genuine rank-eight target order;
2. a non-P/Q equality compiler;
3. another K15 parent or lift; or
4. a length-12873 K16 word globally.

Thus a genuine-four-filter continuation must change the target chronology
while repairing (2.2)--(2.4), or change the compiler architecture. K-best
enumeration of schedules for the unmodified order cannot overcome the
579-unit global scalar gap.

The independent binder is

```text
scratch/audit_threadA_k16_true_fourfilter_natural_20260731.py
scratch/threadA_k16_true_fourfilter_natural_20260731.audit.json
```
