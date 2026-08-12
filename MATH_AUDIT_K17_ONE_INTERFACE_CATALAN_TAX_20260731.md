# The certified \(k=17\) upper word pays exactly the one-interface Catalan tax

Date: 2026-07-31  
Status: exact literal audit and exact architecture-scoped lower bound

## 1. Coordinate restriction gives the lower bound

For any universal word \(A\) on \([k]\) and coordinate \(z\), delete every
letter containing \(z\).  Every target avoiding \(z\) had a witnessing
interval wholly inside one \(z\)-free run.  After the runs are concatenated,
all those witnesses remain intervals.  Therefore the retained word is
universal on \([k-1]\), and

\[
 \#\{i:z\notin A_i\}\ge\nu(k-1).                              \tag{1.1}
\]

If all \(z\)-free entries form one block and all \(z\)-containing entries
form the other block, the first block has length at least \(\nu(k-1)\).
The marked middle antichain additionally needs at least
\(W(k-1)\) distinct endpoints in the second block.  Hence every such
one-interface lift has

\[
                         |A|\ge\nu(k-1)+W(k-1).                 \tag{1.2}
\]

At \(k=17\), using the proved \(\nu(16)=12873\),

\[
 \nu(16)+W(16)=12873+12870=25743.                              \tag{1.3}
\]

Since

\[
 B(17)=24313,\qquad \operatorname{Cat}_8=1430,
\]

the exact one-interface tax is

\[
                   25743-B(17)=1430=\operatorname{Cat}_8.      \tag{1.4}
\]

Thus no local shortening of a separated two-rail construction can prove the
conjectured value.  The Catalan saving is exactly the number of positions
that must be recovered by interleaving the two coordinate sectors.

## 2. Literal anatomy of the retained word

The certified word “answers/k17_upper25746.word” has exactly two top-bit
runs:

\[
                         0^{12873}1^{12873}.                    \tag{2.1}
\]

Its first-middle scan has:

\[
 \begin{array}{c|c}
 \text{quantity}&\text{value}\\ \hline
 \text{first-middle starts}&25743=25746-3\\
 \text{distinct rank-nine labels}&24310=W(17)\\
 \text{duplicate first-middle occurrences}&1433\\
 \text{target multiplicities}&1^{22979}2^{1230}3^{100}4^1\\
 \text{first-middle widths}&2^2 3^{6388}4^{12869}5^{6484}
 \end{array}                                                   \tag{2.2}
\]

The duplicate count is exactly

\[
                 1433=25746-3-W(17)=\operatorname{Cat}_8+d(17).
                                                                    \tag{2.3}
\]

Of these duplicates, 1,429 are unmarked and four are seam-marked.  They are
not 1,433 disposable letters: the entire \(z\)-free block already has the
minimum possible length \(\nu(16)=12873\).  Removing any net position from
that block would leave too few \(z\)-free letters to cover the old cube.

The retained construction is therefore already only three positions above
the sharp lower bound for its one-interface architecture:

\[
                         25746-25743=3=d(17).                    \tag{2.4}
\]

This explains both its closeness and why it does not directly compress to
\(B(17)\).  The missing operation is global: redistribute marked occurrences
through the optimal \(k=16\) clean chronology so that the same physical
positions serve both Pascal sectors.  A collar or isolated seam repair cannot
recover the Catalan term.

## 3. Equality incidence constraint

Equation (1.1) also gives, for every coordinate \(z\) in a hypothetical
length-\(B(17)\) word,

\[
 \#\{i:z\in A_i\}
   \le B(17)-\nu(16)
   =11440
   =\binom{16}{9}.                                             \tag{3.1}
\]

Summing over coordinates,

\[
                         \sum_i|A_i|\le17\binom{16}{9}.         \tag{3.2}
\]

The number \(11440\) is exactly the unmarked Pascal-sector size in the
rank-nine decomposition

\[
 \binom{[17]}9
 =\binom{[16]}9\ \sqcup\
   \bigl(\{z\}+\binom{[16]}8\bigr).                            \tag{3.3}
\]

This does **not** force a two-block or flat carrier normal form: (3.1) is an
upper frequency bound and can have slack.  It does prove that an exact
Pascal induction must reuse clean positions across many marked witnesses;
there is no room for a second full parent copy.

## 4. Authentication

The replay files are:

    scratch/audit_k17_one_interface_catalan_tax_20260731.py
    scratch/k17_one_interface_catalan_tax_20260731.audit.json

It independently scans the first rank-nine occurrence from every physical
start and verifies all identities above.  Its scope is the retained
one-interface word and the architecture lower bound (1.2); it makes no
global claim that \(\nu(17)>B(17)\).

