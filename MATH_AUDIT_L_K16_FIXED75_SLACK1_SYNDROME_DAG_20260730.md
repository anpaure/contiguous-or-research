# K16 fixed-D4 75-block: exact scope and five-triple slack-one syndrome-DAG obstruction

Date: 2026-07-30

## 0. Verdict

The reduction from the denominator-four primal to a `621`-arc slack-one
problem is **not global**.  It is exhaustive only on the following face:

1. retain exactly the four named D4 support cycles of types
   $3C_{15}+C_{30}$, hence exactly the frozen 75 seams;
2. retain separated-port capacity against that block, so every added seam
   avoids all 75 ports occupied by it;
3. use exactly 30 further seams;
4. impose the count-105 direct-dual ledger with total slack $R=1$, hence
   repeat weight $Q=2$.

Here and below $Q$ denotes repeated target price and $R$ denotes direct
dual slack, so

\[
                              Q+R=3.                    \tag{0.1}
\]

On this face, no nonnegative balanced residual circulation exists.  The
proof is solver-free: a five-bit syndrome propagation through the exact tight
SCC condensation shows that every slack-one portal cycle has syndrome of
Hamming weight one, whereas every allowed $Q=2$ service profile has
syndrome of Hamming weight three or five.

This eliminates the fixed-D4-75, $Q=2,R=1$ face.  It does **not** eliminate
all count-105 selections, all global slack-one selections, a different choice
of 75 seams, a residual packet allowed to reuse a fixed port, or another seam
catalogue.  A separate 1,741-portal global directed-path audit may support a
wider slack-one statement, but that artifact is neither assumed nor audited
here.

## 1. Frozen data and direct accounting

For a seam $e:u\to v$, let $H(e)$ be its set of serviced frozen targets.
The authenticated scale-two certificate gives prices

\[
 b_t\in\{1,2,4\},\qquad \sum_t b_t=207,
\]

and an integer port potential $y$ such that

\[
 s(e):=2+y_v-y_u-\sum_{t\in H(e)}b_t\ge0              \tag{1.1}
\]

for all 211,604 raw seams.  For any balanced count-105 integral selection
$x$, potential telescoping gives

\[
 210=\sum_t b_t\mu_t+\sum_e s(e)x_e
    =207+Q+R,                                           \tag{1.2}
\]

where

\[
 Q=\sum_t b_t(\mu_t-1),\qquad
 R=\sum_e s(e)x_e.                                     \tag{1.3}
\]

Thus $Q+R=3$.  In the branch $R=1$, necessarily $Q=2$, and exactly one
selected seam has slack one; all other selected seams are tight.

The exhaustive $Q=2$ multiplicity profiles are:

* one extra occurrence of one of the 60 price-two targets;
* two extra occurrences of one of the 15 price-one targets;
* one extra occurrence of each of two distinct price-one targets.

There are

\[
                         60+15+\binom{15}{2}=180        \tag{1.4}
\]

profiles.

## 2. What exactly is fixed

The raw D4 replay has 174 supported seams with total numerator 414.  Its
simple support is a disjoint union of eight directed cycles with types

\[
 3(C_{15},4),\quad (C_{30},3),\quad (C_{45},2),
 \quad3(C_{18},1),                                     \tag{2.1}
\]

where the second coordinate is the constant numerator on that cycle.

The fixed block is precisely the three $C_{15}$'s of numerator four and
the $C_{30}$ of numerator three.  Raw replay verifies:

\[
 |E_0|=75,\qquad |V(E_0)|=75,                          \tag{2.2}
\]

the block is balanced and capacity one, and it services exactly 60 targets,
each once.  Their price histogram is

\[
                         45\cdot2+15\cdot4.             \tag{2.3}
\]

Consequently all 15 price-one targets remain outside the block.  The 33
residual targets have price histogram

\[
                         15\cdot1+15\cdot2+3\cdot4=57. \tag{2.4}
\]

If the combined selection is port-capacitated and retains $E_0$, every
residual seam must avoid the 75 fixed ports.  Since $Q=2$, a residual seam
hitting any already serviced price-four target is impossible.  These two
necessary deletions are exactly the conditioning used below.

They are also the reason the reduction is not global.  A general
service-plus-balance selection need not contain $E_0$, and a model omitting
port capacity need not avoid its ports even if its seam IDs are artificially
held fixed.

## 3. Exact 107-portal and 621-arc reduction

After removing seams touching the 75 fixed ports and seams hitting a fixed
price-four target, the raw ledger contains

\[
 40,530\text{ tight arcs},\qquad 32,978\text{ slack-one arcs}. \tag{3.1}
\]

Let $G_0$ be the directed graph of those 40,530 tight arcs.  If a balanced
nonnegative residual circulation has total slack one, its unique slack-one
arc $e:u\to v$ lies on a directed closed walk.  Removing $e$ from that
walk leaves a directed tight path from $v$ to $u$.  Therefore $e$ is
admissible only when

\[
                 [v]\leadsto[u]                         \tag{3.2}
\]

in the SCC condensation of $G_0$.

Exact bitset reachability on the 12,612-node condensation leaves precisely
107 slack-one seam IDs.  Hence the necessary graph has

\[
                       40,530+107=40,637                 \tag{3.3}
\]

arcs.  Every positive arc of a finite balanced nonnegative circulation lies
on a directed cycle.  Deleting every arc outside a cyclic SCC of this graph
therefore loses no feasible residual circulation.  Exactly 621 arcs remain:

\[
             514\text{ tight}+107\text{ slack-one},     \tag{3.4}
\]

of which 426 service at least one frozen target.

The independent standard-library replays agree on the exact eligible seam-ID
hash

```text
37c5bfad39375c3c6d405ea03c96db9e308cc8efcaec6c12924adf5fae8b99ee
```

and on the portal-ID hash

```text
5b99f9bc09a74c6337b9ad200efda9fdb333ec876c8daf3e58bd86ecbbb35771
```

### Lemma 3.1 (scope-exact cyclic-core reduction)

Every port-capacitated count-105 selection that contains the frozen block
$E_0$ and lies in the branch $Q=2,R=1$ has all its other 30 seams among
the displayed 621 arcs.

#### Proof

The fixed block is itself balanced.  Subtracting it leaves a balanced
nonnegative 30-seam circulation on ports disjoint from $V(E_0)$.  Equations
(1.2)--(1.3) give one slack-one seam and 29 tight seams.  No selected residual
seam can repeat a fixed price-four target.  The unique slack-one seam has a
tight return path, proving the 107-portal restriction.  Every selected seam
lies on a directed cycle of the tight-plus-portal graph, proving the cyclic
SCC restriction.  QED.

Notice what the lemma does not say: the 621 arcs are not an exhaustive bank
for a count-105 solution that changes the fixed block or shares one of its
ports.

## 4. Five price-one triples

Partition the 15 price-one targets into

\[
\begin{aligned}
 T_0&=\{35044,36935,40066\},\\
 T_1&=\{37320,41102,47364\},\\
 T_2&=\{33906,36417,51235\},\\
 T_3&=\{33337,50976,58385\},\\
 T_4&=\{41872,49436,61960\}.
\end{aligned}                                           \tag{4.1}
\]

For any seam $e$, define its five-bit syndrome

\[
 \sigma(e)_j=|H(e)\cap T_j|\pmod2.                      \tag{4.2}
\]

The verifier does not import a precomputed lattice basis.  It reparses the
raw seams, hard-codes only the target triples (4.1), and independently checks
that they partition exactly the 15 price-one targets.

Within every SCC of $G_0$, it constructs a phase

\[
                         \phi:V\to\mathbb F_2^5         \tag{4.3}
\]

satisfying, on every tight arc whose endpoints lie in that SCC,

\[
                         \sigma(u\to v)=\phi(u)+\phi(v).\tag{4.4}
\]

The replay checks (4.4) on all 315 internal tight arcs.  Therefore every
directed all-tight closed walk has syndrome zero.

For a tight arc between different SCCs define the reduced label

\[
 \bar\sigma(u\to v)=\phi(u)+\sigma(u\to v)+\phi(v).     \tag{4.5}
\]

The condensation is a DAG.  A 32-state dynamic program propagates all exact
XOR sums of (4.5) from each of the 56 portal-head SCCs.  Restoring endpoint
phases and adding the portal's own syndrome gives every possible syndrome of
every portal-plus-tight-return closed walk.

### Lemma 4.1 (exact portal syndrome set)

Across all 107 portals and every directed tight return path, the attainable
closed-walk syndromes are exactly

\[
                    \{00001,00010,00100,01000,10000\}.  \tag{4.6}
\]

In particular every such syndrome has Hamming weight one.

This is a finite exact DAG calculation, not a shortest-path heuristic.  The
full 107-row portal table is stored in the audit artifact; its stable hash is

```text
ef0c8d2fe7cd6d419d8e6893cdf74db79adbbb7804ed9284d9ce1f94ca5091f7
```

## 5. All repeat-weight-two parities

Each $T_j$ contains three targets.  Servicing every target once gives
baseline syndrome

\[
                              11111.                    \tag{5.1}
\]

The 180 exact $Q=2$ profiles from (1.4) collapse as follows.

1. Repeating one price-two target adds no bit in (4.2), so the syndrome is
   `11111`.
2. Repeating one price-one target twice toggles the same bit twice, again
   giving `11111`.
3. Repeating two distinct price-one targets toggles two bits.  If they belong
   to the same triple, those toggles cancel and again give `11111`.  If they
   belong to different triples, exactly two baseline bits are cleared.

Thus the complete allowed syndrome set is

\[
 \mathcal A=\{11111\}\cup
 \{11111\oplus e_i\oplus e_j:0\le i<j<5\}.             \tag{5.2}
\]

It consists of one word of weight five and all ten words of weight three:

```text
00111 01011 01101 01110 10011 10101
10110 11001 11010 11100 11111
```

By (4.6),

\[
          \mathcal A\cap\{00001,00010,00100,01000,10000\}
          =\varnothing.                                 \tag{5.3}
\]

## 6. Fixed-face no-go theorem

### Theorem 6.1

There is no nonnegative integral balanced 30-seam residual circulation on
ports disjoint from the frozen D4 block $E_0$ which, together with $E_0$,
has count 105, services all 93 targets, and has direct ledger
$Q=2,R=1$.

The conclusion remains true after imposing residual port capacity, because
the proof has relaxed that condition.

#### Proof

Suppose such a residual circulation exists.  Its unique slack-one seam lies
on a closed selected component and has a tight return path.  Every other
selected component is an all-tight directed closed walk.  By (4.4), all the
all-tight components have syndrome zero.  Therefore the syndrome of the full
residual circulation is the syndrome of the portal-plus-return closed walk,
hence has weight one by Lemma 4.1.

On the other hand, exact service and repeat weight two force its syndrome to
belong to (5.2), hence to have weight three or five.  This contradicts (5.3).
QED.

### Why ordinary lattice elimination does not prove this

As an adversarial check, a separate program constructs all 530 balance,
service, count and slack rows on the 621 columns and computes row-space
relations modulo

\[
                            2,3,5,7,11,13.              \tag{6.1}
\]

Every one of the 180 exact right-hand sides survives every test.  The matrix
has rank 502 and 28 left-null relations over each listed field.  Hence there
is no modular contradiction in this bank at these primes.  The decisive
ingredient is directed nonnegative path chronology in the SCC condensation,
not signed cycle-lattice torsion.

## 7. Scope boundary for constructive count 105

This theorem says only that the particular integral block
$3C_{15}+C_{30}$ cannot be completed by a disjoint 30-seam packet in the
slack-one branch.  A constructive count-105 attack must do at least one of:

1. recolour/recombine the D4 cycles before freezing 75 seams;
2. choose a different 75-seam block;
3. work in a different restitution branch $R=0,2,3$ when not already
   excluded elsewhere;
4. abandon this source-relative catalogue.

The result supplies no q1, separation, reverse-edge, residence, survivor,
all-depth, or compiler certificate.  Those stronger rows were not needed for
the no-go.  No candidate witness is produced on this face, so the canonical
full candidate checker has no input to replay.

## 8. Reproduction and frozen hashes

The exact no-go replay is

```text
python3 scratch/audit_l_k16_fixed75_s1_syndrome_dag_20260730.py \
  --binary scratch/k16_len8_source_seam_ledger_20260730.bin \
  --certificate scratch/k16_direct_cut_dual_scale2_floor104_20260730.audit.json \
  --fixed75-audit scratch/l_k16_d4_cycle_blocks_20260730.audit.json \
  --output NEW_FIXED75_SYNDROME_DAG_AUDIT.json
```

It uses only the Python standard library.  The certified H100 replay used one
CPU, 1.07 seconds wall time, 86,128 KiB maximum RSS, and a 512 MiB virtual
memory cap.  A second invocation emitted a byte-identical audit JSON with
SHA-256 `41567cde...53f04`.

```text
raw seam ledger
  scratch/k16_len8_source_seam_ledger_20260730.bin
  832ddd883452e73c0f2462f8550e900d8ffcf01f7397f17b980dd552853b6657

scale-two certificate
  scratch/k16_direct_cut_dual_scale2_floor104_20260730.audit.json
  a89f9166a1f6eade1db20ea3b76d15aad2187eac48e23e0566b6968972b18bb2

D4 fixed-block audit
  scratch/l_k16_d4_cycle_blocks_20260730.audit.json
  b9dca4325deac03fa8575ad755db2cf54b777f1dd8811009d2e35f25e5eaa7a8
  embedded payload 71b41ba55eca841184f5b87a7221cbae384965f6242fb8595b29459ad8816d57

five-triple syndrome-DAG driver
  scratch/audit_l_k16_fixed75_s1_syndrome_dag_20260730.py
  42e1e72270ff80ba2dbbe30ea9bb197bd178289aef264c81bcefbeafcdc8cc0d

five-triple syndrome-DAG audit
  scratch/l_k16_fixed75_s1_syndrome_dag_v2_20260730.audit.json
  41567cde5baed2208be1e8dcfea23e0a84f35b066b471cfa2c63b31d7f453f04
  embedded payload 0c360fd5af1da0656a6647b86ce0d1f7b42177e0e18b3758328a66acb720be14

deterministic replay stdout / resource ledger
  scratch/l_k16_fixed75_s1_syndrome_dag_v2_20260730.stdout.txt
  f34eb7e273f1affb3b1a39198e732f97e7d3f98d64a20d5435ede086ce31df2d
  scratch/l_k16_fixed75_s1_syndrome_dag_v2_20260730.resource.txt
  44620597817ea48c2ce2d40c6c4f0dba3d9439ebb6c7d26d47f18f4b2aac8c58

independent 621-column modular cross-audit driver
  scratch/audit_l_k16_fixed75_s1_parity_20260730.py
  d9d8e5eeb18b641a4416506be8d85d3b7a78d72534a94d5940a53f9fae010bc0

independent 621-column modular cross-audit
  scratch/l_k16_fixed75_s1_modular_independent_20260730.audit.json
  9dc8f7105bde6ff5832a8b89da063d7d34b64b4e59d7cb9abc58b0dbc5b06e6a
  embedded payload 38c8d8099a9c00bf23528ea6ab2b2b882cf8f4a19e6c88d7bb480daa07a0ff14
```

The two independent parsers agree on the fixed block dimensions, 107 portal
IDs, 621 cyclic seam IDs, slack histogram `514/107`, provider count 426, and
eligible seam-ID hash.  The modular audit's survival of all 180 branches is a
negative control; it is not used to prove Theorem 6.1.
